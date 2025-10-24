# Gate G5 – Stage 5 Hardening 합격 기준

1. **규칙 린트 통과**: `python scripts/rule_linter.py` 실행 결과 용어 불일치, 우선순위 역전, 링크 누락이 0건이어야 한다.
2. **패치 커버리지**: `reports/patch_coverage.md`가 Stage 4 `failure_cases.md`의 항목 중 ≥80%가 Stage 5 문서로 해결됨을 표와 서술로 입증한다. (현재 목표: 100% 매핑)
3. **감사 보고**: `reports/audit_report.md`가 권고/경고 항목마다 대응하는 Stage 5 패치 섹션 링크를 명시한다.
4. **데이터 불변성**: `scripts/rule_linter.py`, `scripts/audit_annotations.py`는 어떤 주석 파일도 생성·수정하지 않으며, README의 실행 순서가 이를 재확인한다.
5. **문서 일관성**: Stage 5 보강 문서에 등장하는 용어, 우선순위, 감정 구름 라벨은 Stage 0–3에서 고정한 목록과 일치해야 한다.
