#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
INPUT="$ROOT_DIR/diagrams/lode_overview.mmd"
OUTPUT="$ROOT_DIR/diagrams/lode_overview.png"
PUPPETEER_CONFIG="$ROOT_DIR/diagrams/puppeteer-config.json"

if ! command -v mmdc >/dev/null 2>&1; then
  echo "[export_diagram] Mermaid CLI (mmdc) not found. Install @mermaid-js/mermaid-cli first." >&2
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "[export_diagram] Input file not found: $INPUT" >&2
  exit 1
fi

mmdc -i "$INPUT" -o "$OUTPUT" --scale 1.25 --backgroundColor '#ffffff' -p "$PUPPETEER_CONFIG"
echo "Diagram exported to $OUTPUT"
