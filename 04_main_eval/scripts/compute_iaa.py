#!/usr/bin/env python3
"""Compute pilot inter-annotator agreement for scope, discourse, and counter-current axes."""

import json
import sys
from collections import defaultdict
from pathlib import Path

AXES = {
    "Scope-Consistency": "scope_rings",
    "Discourse-Edge Coverage": "discourse_links",
    "Counter-Current Preservation Rate": "counter_current_flags",
}


def load_annotations(path: Path) -> dict[str, dict]:
    data: dict[str, dict] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            data[record["document_id"]] = record
    return data


def to_scope_tuple(ring: dict) -> tuple:
    span = ring.get("span", {})
    return (
        span.get("start"),
        span.get("end"),
        ring.get("priority"),
        ring.get("label"),
    )


def to_discourse_tuple(link: dict) -> tuple:
    return (
        link.get("type"),
        link.get("source_sentence"),
        link.get("target_sentence"),
    )


def to_counter_tuple(flag: dict) -> tuple:
    return (
        flag.get("sentence_index"),
        flag.get("type"),
        flag.get("focus"),
    )


CASTERS = {
    "Scope-Consistency": to_scope_tuple,
    "Discourse-Edge Coverage": to_discourse_tuple,
    "Counter-Current Preservation Rate": to_counter_tuple,
}


def percent_agreement(set_a: set, set_b: set) -> float:
    if not set_a and not set_b:
        return 1.0
    if not set_a or not set_b:
        return 0.0
    intersection = set_a & set_b
    return (2 * len(intersection)) / (len(set_a) + len(set_b))


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: compute_iaa.py <annotator_A.jsonl> <annotator_B.jsonl>", file=sys.stderr)
        return 1

    path_a = Path(argv[1])
    path_b = Path(argv[2])

    if not path_a.exists() or not path_b.exists():
        print("Input files must exist", file=sys.stderr)
        return 1

    data_a = load_annotations(path_a)
    data_b = load_annotations(path_b)
    docs = sorted(set(data_a) & set(data_b))
    if not docs:
        print("No overlapping document IDs", file=sys.stderr)
        return 1

    axis_scores: dict[str, list[float]] = defaultdict(list)
    doc_rows: list[dict[str, float]] = []

    for doc_id in docs:
        row: dict[str, float] = {"document_id": doc_id}
        for axis, field in AXES.items():
            caster = CASTERS[axis]
            set_a = {caster(item) for item in data_a[doc_id].get(field, [])}
            set_b = {caster(item) for item in data_b[doc_id].get(field, [])}
            score = percent_agreement(set_a, set_b)
            axis_scores[axis].append(score)
            row[axis] = score
        doc_rows.append(row)

    print("IAA per document:")
    header = ["Document"] + list(AXES.keys())
    print("\t".join(header))
    for row in doc_rows:
        values = [row["document_id"]] + [f"{row[axis]:.2f}" for axis in AXES]
        print("\t".join(values))

    print("\nAxis averages:")
    overall_sum = 0.0
    for axis in AXES:
        scores = axis_scores[axis]
        avg = sum(scores) / len(scores) if scores else 0.0
        print(f"{axis}: {avg:.2f}")
        overall_sum += avg
    overall_average = overall_sum / len(AXES)
    print(f"\nOverall macro-average: {overall_average:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
