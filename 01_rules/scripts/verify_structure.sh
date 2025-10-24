#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required_files=(
  "README.md"
  "guidelines/sentence_linearization.md"
  "guidelines/paragraph_document_linearization.md"
  "guidelines/scope_priority.md"
  "guidelines/discourse_inventory.md"
  "guidelines/counter_current_preservation.md"
  "guidelines/capsules_and_aux_bridges.md"
  "templates/annotation_template.jsonl"
  "templates/rubric_checklist.md"
  "protocols/annotation_protocol.md"
  "protocols/adjudication_guidelines.md"
  "success_criteria/gate_G1.md"
  "success_criteria/metrics_addendum.md"
)

missing=()
for file in "${required_files[@]}"; do
  if [ ! -f "$ROOT_DIR/$file" ]; then
    missing+=("$file")
  fi
done

if [ ${#missing[@]} -ne 0 ]; then
  printf 'Missing required files:\n'
  for file in "${missing[@]}"; do
    printf ' - %s\n' "$file"
  done
  exit 1
fi

echo "All required files are present."
