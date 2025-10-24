#!/usr/bin/env python3
"""Validate annotation JSONL files against Stage 1 template fields."""

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "document_id",
    "source_metadata",
    "tokens",
    "line_nodes",
    "operators",
    "scope_rings",
    "discourse_links",
    "page_current",
    "ribbon_axis",
    "counter_current_flags",
    "capsules",
    "auxiliary_bridges",
    "emotion_clouds",
    "surface_rail_notes",
    "validation_checks",
    "review_status",
]

MANDATORY_SOURCE_KEYS = {"genre", "source_path", "license"}

def validate_entry(entry: dict, index: int, path: Path) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in entry:
            errors.append(f"{path}:{index}: missing field '{field}'")
    # If a required field is present but empty, ensure reviewer noted rationale when applicable
    if "validation_checks" in entry and not isinstance(entry["validation_checks"], dict):
        errors.append(f"{path}:{index}: validation_checks must be an object")
    if "source_metadata" in entry:
        meta = entry["source_metadata"]
        if not isinstance(meta, dict):
            errors.append(f"{path}:{index}: source_metadata must be an object")
        else:
            missing = MANDATORY_SOURCE_KEYS - set(meta.keys())
            if missing:
                errors.append(f"{path}:{index}: source_metadata missing keys {sorted(missing)}")
    # Ensure tokens non-empty text
    if isinstance(entry.get("tokens"), list):
        if not entry["tokens"]:
            errors.append(f"{path}:{index}: tokens list is empty")
    else:
        errors.append(f"{path}:{index}: tokens must be a list")
    # Ensure arrays present even if empty
    for field in ("line_nodes", "operators", "scope_rings", "discourse_links",
                  "counter_current_flags", "capsules", "auxiliary_bridges", "emotion_clouds"):
        value = entry.get(field)
        if not isinstance(value, list):
            errors.append(f"{path}:{index}: field '{field}' must be a list")
    return errors

def main(paths: list[str]) -> int:
    if not paths:
        print("Usage: validate_schema.py <annotation.jsonl> [...]", file=sys.stderr)
        return 1
    exit_code = 0
    for name in paths:
        path = Path(name)
        if not path.exists():
            print(f"Missing file: {path}", file=sys.stderr)
            exit_code = 1
            continue
        with path.open(encoding="utf-8") as handle:
            for idx, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError as exc:
                    print(f"{path}:{idx}: JSON decode error: {exc}", file=sys.stderr)
                    exit_code = 1
                    continue
                errors = validate_entry(entry, idx, path)
                for msg in errors:
                    print(msg, file=sys.stderr)
                    exit_code = 1
    if exit_code == 0:
        print("Schema validation passed for", ", ".join(paths))
    return exit_code

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
