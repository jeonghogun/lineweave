# 04_main_eval — Stage 4 Main Evaluation Round

Stage 4 confirms that the Stage 3 refinements raise inter-annotator agreement on fresh material without altering the schema. Two annotators independently applied the Stage 1 template and Stage 3 clarifications to 30 public-domain documents (10 news reportage, 10 editorial essays, 10 dialogues). The workflow captures pre- and post-adjudication metrics, coverage audits, and remaining issues for Stage 5 follow-up.

## Local Workflow
1. **Data hygiene**
   - Collect only public-domain or government texts that were *not* used in Stage 2.
   - Record source metadata in `data/sources.md` with URL and license before annotating.
   - Remove Project Gutenberg boilerplate, headers, and trailing license notices.
2. **Annotation**
   - Use `01_rules/templates/annotation_template.jsonl` as the schema contract.
   - Apply Stage 3 documents in the following order during review: `changes/discourse_refinement.md` → `changes/scope_modal_tense_resolution.md` → `changes/counter_current_checks.md` → `changes/emotion_cloud_lexicon.md`.
   - Produce `annotations/annotator_A.jsonl` and `annotations/annotator_B.jsonl` independently. Do not share intermediate notes prior to the initial IAA run.
   - If adjudication is required, perform a single pass guided by `03_rule_refine/checklists/adjudication_quickref.md` and save the outcome to `annotations/adjudicated.jsonl`.
3. **Validation scripts** (read-only checks)
   - `python scripts/validate_schema.py annotations/annotator_*.jsonl`
   - `python scripts/compute_iaa.py annotations/annotator_A.jsonl annotations/annotator_B.jsonl > reports/iaa_main.md`
   - `python scripts/coverage_report.py annotations/annotator_A.jsonl annotations/annotator_B.jsonl > reports/coverage_stats.md`
   These utilities only read JSONL files and emit reports; they never create or modify annotation data.
4. **Report assembly**
   - Summarize IAA deltas vs. Stage 2 inside `reports/iaa_main.md`.
   - Capture distribution checks in `reports/coverage_stats.md` to surface skew or sampling gaps.
   - Document unresolved ambiguities (10–15 entries) in `reports/failure_cases.md`, linking each case to the relevant Stage 3 rule and proposing a Stage 5 remedy.

## Pre-Submission Checklist
- [ ] All 30 raw documents exist under `data/raw/` with accurate sourcing.
- [ ] Annotation files respect every field defined in `annotation_template.jsonl`.
- [ ] `scripts/validate_schema.py` and `scripts/compute_iaa.py` run without error.
- [ ] Discourse axis IAA improves by ≥ +0.10 absolute over Stage 2 and overall macro-average ≥ 0.80.
- [ ] Coverage report includes discourse, scope, counter-current, and emotion counts.
- [ ] `success_criteria/gate_G4.md` is satisfied and referenced in `reports/iaa_main.md`.
- [ ] Validation section in the Stage 4 response explicitly addresses data licensing, guideline usage, metric improvement, tool read-only behavior, and remaining ambiguities.
