#!/usr/bin/env python3
"""Stage 5 annotation audit (read-only).

Consumes Stage 4 annotation JSONL files and emits a markdown report summarising
potential rule violations that the Stage 5 patches are meant to resolve.
The script never writes to the annotation files; it only reads them and prints
findings to stdout.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

CATEGORY_DOC_LINK = {
    "tie_breaker": ("Result vs elaboration evidence requires Stage 5 tie-breaker cues.", "changes/discourse_tie_breakers.md#1-result-vs-elaboration-lexical-cues"),
    "because_branch": ("Because/so clauses with modals should follow the deontic-causal branch.", "changes/causal_modal_edge_cases.md#2-deontic-vs-causal-branch"),
    "counter_strength": ("Counter-current flags need soft/strong notes per Stage 5 guidance.", "changes/counter_current_strength.md#1-strength-layers"),
    "evidence_scope": ("Evidence spans should include clause quotes and scope IDs.", "changes/evidence_span_guidelines.md#1-clause-granularity"),
    "question_transition": ("Question-shaped sentences should follow the transition primer.", "changes/question_quote_rules.md#1-question-led-transitions"),
    "emotion_default": ("Hedged tones should default to calm/concern per Stage 5 rule.", "changes/question_quote_rules.md#2-emotion-cloud-defaults"),
    "quote_boundary": ("Quotation marks require scope boundary confirmation.", "changes/question_quote_rules.md#3-quote-boundary-scope"),
    "dialog_chain": ("Dialogue turns need chain IDs per Stage 5 dialog notes.", "changes/dialog_chain_notes.md#1-chain-linking"),
    "ribbon_scale": ("Dialogue persuasion should use the micro-scale guidance.", "changes/dialog_chain_notes.md#2-ribbon-micro-scale"),
    "surface_macro": ("Surface rail notes should follow the Stage 5 macro template.", "changes/surface_rail_macros.md#2-macro-prompt-structure"),
}

MODALS = {"should", "must", "can", "could", "may", "might", "ought", "need"}
CAUSAL_CUES = {"because", "since", "따라서", "그러므로", "so"}
HEDGING = {"might", "perhaps", "seems", "maybe", "could"}
PERSUASION = {"should", "must", "convince", "persuade", "urge", "insist"}
QUOTES = {'"', "''", "“", "”", "'"}


def load_jsonl(path: Path) -> Iterable[dict]:
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def has_modal(tokens: list[str]) -> bool:
    return any(token.lower() in MODALS for token in tokens)


def has_causal(text: str) -> bool:
    lowered = text.lower()
    return any(cue in lowered for cue in CAUSAL_CUES)


def collect_annotations(paths: list[Path]) -> list[dict]:
    records: list[dict] = []
    for path in paths:
        records.extend(load_jsonl(path))
    return records


def main(argv: list[str]) -> int:
    if len(argv) < 1:
        print("Usage: audit_annotations.py <annotation.jsonl> [...]", file=sys.stderr)
        return 1

    paths = [Path(arg) for arg in argv]
    records = collect_annotations(paths)
    findings: dict[str, list[tuple[str, str]]] = defaultdict(list)

    for record in records:
        doc_id = record.get("document_id", "unknown")
        tokens = record.get("tokens", [])
        token_text = " ".join(tokens).lower()

        # 1. tie-breaker: elaboration with causal cues
        for link in record.get("discourse_links", []):
            link_type = link.get("type", "").lower()
            evidence = link.get("evidence", "")
            if link_type == "elaboration" and has_causal(evidence):
                findings["tie_breaker"].append((doc_id, f"Elaboration link {link.get('id')} cites causal cue '{evidence[:60]}…'"))
            if link_type in {"result", "cause"} and not has_causal(evidence):
                if has_causal(token_text):
                    findings["because_branch"].append((doc_id, f"Link {link.get('id')} lacks explicit causal evidence despite modal/causal tokens."))
            if link_type in {"result", "cause"} and has_modal(tokens) and not has_causal(evidence):
                findings["because_branch"].append((doc_id, f"Link {link.get('id')} mixes modals without citing causal span."))
            if len(evidence) < 80 or "tokens[" not in evidence:
                findings["evidence_scope"].append((doc_id, f"Link {link.get('id')} evidence too short or missing token span."))

        # 2. counter-current strength logging
        for flag in record.get("counter_current_flags", []):
            note_text = (flag.get("reason") or "") + " " + (flag.get("notes") or "")
            if "strength" not in note_text.lower():
                findings["counter_strength"].append((doc_id, f"Flag {flag.get('id')} missing soft/strong note."))

        # 3. question-led transitions & quote boundary
        if "?" in tokens and not any(link.get("type") in {"shift", "transition"} for link in record.get("discourse_links", [])):
            findings["question_transition"].append((doc_id, "Question mark present without shift/transition link."))

        if any(token in QUOTES for token in tokens):
            quote_notes = record.get("surface_rail_notes", "") + " " + " ".join(record.get("notes", []) if isinstance(record.get("notes"), list) else [])
            if "quote boundary" not in quote_notes.lower():
                findings["quote_boundary"].append((doc_id, "Quotation detected without quote boundary note."))

        # 4. emotion cloud defaults
        has_hedge = any(token.lower() in HEDGING for token in tokens)
        emotion_entries = record.get("emotion_clouds", [])
        if has_hedge and not emotion_entries:
            findings["emotion_default"].append((doc_id, "Hedging verbs present but emotion cloud not set."))

        # 5. dialogue chain & ribbon scale & macro
        genre = (record.get("source_metadata", {}).get("genre") or "").lower()
        if genre == "dialogue":
            links = record.get("discourse_links", [])
            unique_sentences = set()
            for link in links:
                if "source_sentence" in link:
                    unique_sentences.add(link["source_sentence"])
                if "target_sentence" in link:
                    unique_sentences.add(link["target_sentence"])
            if len(links) + 1 < len(unique_sentences):
                findings["dialog_chain"].append((doc_id, "Dialogue turn count exceeds link coverage."))
            ribbon_segments = record.get("ribbon_axis", {}).get("segments", [])
            if any(abs(seg.get("value", 0)) < 0.25 for seg in ribbon_segments) and any(token.lower() in PERSUASION for token in tokens):
                findings["ribbon_scale"].append((doc_id, "Persuasion cues present but ribbon magnitude below 0.25."))

        # 6. surface rail macro usage
        notes_text = (record.get("surface_rail_notes") or "").lower()
        if "surface rail audit:" not in notes_text:
            findings["surface_macro"].append((doc_id, "Surface rail macro template not detected."))

    # Deduplicate findings per category/doc/message pair.
    for key, entries in list(findings.items()):
        unique: list[tuple[str, str]] = []
        seen: set[tuple[str, str]] = set()
        for item in entries:
            if item not in seen:
                unique.append(item)
                seen.add(item)
        findings[key] = unique

    print("# Stage 5 Audit Report")
    print()
    print("## Summary")
    for key, (desc, link) in CATEGORY_DOC_LINK.items():
        count = len(findings.get(key, []))
        print(f"- {desc} → {count} 사례 ([{link}]({link}))")

    print()
    print("## Details")
    for key, entries in findings.items():
        if not entries:
            continue
        desc, link = CATEGORY_DOC_LINK[key]
        print(f"### {desc} — [{link}]({link})")
        for doc_id, message in entries:
            print(f"- `{doc_id}`: {message}")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
