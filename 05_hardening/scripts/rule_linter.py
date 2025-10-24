#!/usr/bin/env python3
"""Stage 5 rule consistency linter.

Checks:
- Stage 3 discourse priority string is preserved in Stage 5 tie-breaker doc.
- Stage 1 scope priority string is cited in Stage 5 modal/ evidence docs.
- Emotion cloud labels from Stage 3 appear intact in Stage 5 macro spec.
- Mapping CSV covers every Stage 4 failure id and references valid patch docs.
- Question/quote rules only reference approved emotion labels.
Outputs a markdown summary and exits with status 0 when no conflicts are found.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
STAGE5 = REPO_ROOT / "05_hardening"

PRIORITY_STRING = "반박 > 대조 > 전환 > 인과/결과 > 상세화/예시 > 전개 > 요약"
SCOPE_PRIORITY = "부정 → 모달 → 시제≈상 → 수식"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_stage3_emotions() -> set[str]:
    text = read(REPO_ROOT / "03_rule_refine/changes/emotion_cloud_lexicon.md")
    return set(re.findall(r"\*\*(\w+)\*\*", text))


def extract_stage4_failures() -> set[int]:
    text = read(REPO_ROOT / "04_main_eval/reports/failure_cases.md")
    ids = {int(match) for match in re.findall(r"\|\s*(\d+)\s*\|", text)}
    return ids


def load_mapping_rows() -> list[dict[str, str]]:
    mapping_path = STAGE5 / "mapping/failure_to_patch_map.csv"
    with mapping_path.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return list(reader)


def main() -> int:
    issues: list[str] = []

    tie_text = read(STAGE5 / "changes/discourse_tie_breakers.md")
    if PRIORITY_STRING not in tie_text:
        issues.append("discourse_tie_breakers.md does not restate Stage 3 priority order.")

    modal_text = read(STAGE5 / "changes/causal_modal_edge_cases.md")
    if SCOPE_PRIORITY not in modal_text:
        issues.append("causal_modal_edge_cases.md is missing Stage 1 scope priority string.")

    evidence_text = read(STAGE5 / "changes/evidence_span_guidelines.md")
    if SCOPE_PRIORITY not in evidence_text:
        issues.append("evidence_span_guidelines.md must cite the Stage 1 scope priority order.")

    emotions = extract_stage3_emotions()
    macro_text = read(STAGE5 / "changes/surface_rail_macros.md")
    missing = [label for label in emotions if f"`{label}`" not in macro_text]
    if missing:
        issues.append("surface_rail_macros.md is missing emotion labels: " + ", ".join(sorted(missing)))

    question_text = read(STAGE5 / "changes/question_quote_rules.md")
    q_tokens = set(re.findall(r"`([a-z_]+)`", question_text))
    allowed_inline = emotions | {
        "transition",
        "result",
        "cause",
        "notes",
        "quote",
        "scope",
        "calm",
        "concern",
        "soft",
        "strong",
        "warn",
        "전환",
        "전개",
        "메타발화"
    }
    disallowed = sorted(token for token in q_tokens if token.isalpha() and token not in allowed_inline)
    if disallowed:
        issues.append("question_quote_rules.md references unapproved inline tokens: " + ", ".join(disallowed))

    mapping_rows = load_mapping_rows()
    mapping_ids = {int(row["failure_id"]) for row in mapping_rows}
    stage4_ids = extract_stage4_failures()
    if mapping_ids != stage4_ids:
        missing_ids = stage4_ids - mapping_ids
        extra_ids = mapping_ids - stage4_ids
        if missing_ids:
            issues.append(f"Mapping table missing failure ids: {sorted(missing_ids)}")
        if extra_ids:
            issues.append(f"Mapping table has unknown failure ids: {sorted(extra_ids)}")

    for row in mapping_rows:
        patch_doc = STAGE5 / row["patch_doc"]
        if not patch_doc.exists():
            issues.append(f"Patch document does not exist: {row['patch_doc']}")

    if issues:
        for issue in issues:
            print(f"- [ ] {issue}")
        return 1

    print("- [x] Stage 5 documents preserve Stage 3 discourse priority string.")
    print("- [x] Stage 1 scope priority is cited where modal/evidence rules are refined.")
    print("- [x] Emotion cloud lexicon remains closed across macro and question rules.")
    print("- [x] Mapping table covers all Stage 4 failure cases and points to existing docs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
