#!/usr/bin/env python3
"""Summarize coverage across Stage 4 annotations without modifying data."""

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def load_records(path: Path):
    records = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def summarize(files):
    coverage = defaultdict(lambda: Counter())
    for path in files:
        for record in load_records(path):
            doc_id = record.get("document_id")
            coverage[("documents", None)][path.name] += 1
            # Scope priorities
            for ring in record.get("scope_rings", []):
                coverage[("scope_priority", ring.get("priority"))][path.name] += 1
            # Discourse relation types
            for link in record.get("discourse_links", []):
                coverage[("discourse_type", link.get("type"))][path.name] += 1
            # Counter-current
            for flag in record.get("counter_current_flags", []):
                coverage[("counter_current", flag.get("type"))][path.name] += 1
            # Emotion clouds
            for cloud in record.get("emotion_clouds", []):
                coverage[("emotion_tone", cloud.get("tone"))][path.name] += 1
    return coverage


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize Stage 4 coverage")
    parser.add_argument("files", nargs="+", help="Annotation JSONL files")
    args = parser.parse_args()

    paths = [Path(p) for p in args.files]
    for path in paths:
        if not path.exists():
            raise SystemExit(f"Missing file: {path}")

    coverage = summarize(paths)

    print("# Stage 4 Coverage Summary\n")
    grouped = defaultdict(list)
    for (category, label), counter in coverage.items():
        grouped[category].append((label, counter))

    for category in sorted(grouped):
        print(f"## {category.replace('_', ' ').title()}")
        rows = grouped[category]
        headers = ["Label"] + [p.name for p in paths]
        print("| " + " | ".join(headers) + " |")
        print("| " + " | ".join(["---"] * len(headers)) + " |")
        for label, counter in sorted(rows, key=lambda x: (str(x[0]))):
            row = [str(label if label is not None else "total")] + [str(counter.get(p.name, 0)) for p in paths]
            print("| " + " | ".join(row) + " |")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
