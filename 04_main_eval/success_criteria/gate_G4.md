# Gate G4 — Main Evaluation Pass Criteria

1. **IAA uplift**
   - Discourse-Edge Coverage improves by at least **+0.10 absolute** compared with Stage 2 (target ≥ 0.77 when Stage 2 averaged 0.67).
   - Overall macro-average (Scope, Discourse, Counter-Current) remains **≥ 0.80** before adjudication.
2. **Schema fidelity**
   - `annotation_template.jsonl` fields are present for every document; any field not populated must include an explicit `validation_checks` note describing the exemption.
   - `scripts/validate_schema.py` reports zero missing fields across annotators and adjudicated output.
3. **Coverage reporting**
   - `reports/coverage_stats.md` tabulates scope priorities, discourse tags, counter-current types, and emotion clouds for each annotator file.
4. **Failure analysis**
   - `reports/failure_cases.md` documents at least 10 residual ambiguity cases, none classified as catastrophic (i.e., no unresolved schema violations). Each case cites the Stage 3 rule that will be amended in Stage 5.
5. **Source compliance**
   - `data/sources.md` lists origin, URL, and license for all documents, and no Stage 2 texts are reused.
