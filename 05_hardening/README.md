# Stage 5 – 규칙 패치 & 자동 감사 툴킷

Stage 4 failure log에서 드러난 잔여 문제를 문서 규정으로 보강하고, 기존 주석을 수정하지 않은 채 감사 스크립트로 준수 여부를 점검하는 단계입니다. Stage 0–4에서 정의한 용어와 아이콘을 그대로 유지해야 하며, 모든 산출물은 읽기 전용 검증을 목표로 합니다.

## 산출물 구성
- `changes/`: failure case별 규칙 보강 문서.
- `mapping/failure_to_patch_map.csv`: Stage 4 실패 항목과 Stage 5 패치 문서 매핑.
- `scripts/`: 규칙 린트 및 주석 감사 스크립트(읽기 전용).
- `reports/`: 린트·감사 결과와 패치 커버리지 보고서.
- `success_criteria/gate_G5.md`: 합격 기준.
- `tests/`: 선택 실행 스크립트.

## 로컬 실행 지시
1. (선택) 규칙 린트 스팟 테스트
   ```bash
   bash tests/test_rule_linter.sh
   ```
2. 규칙 일관성 검사 → 결과를 리포트로 저장
   ```bash
   python scripts/rule_linter.py > reports/lint_report.md
   ```
3. 주석 감사(읽기 전용) → Stage 4 주석 파일을 입력
   ```bash
   python scripts/audit_annotations.py ../04_main_eval/annotations/annotator_A.jsonl \
       ../04_main_eval/annotations/annotator_B.jsonl > reports/audit_report.md
   ```
4. 패치 커버리지 요약
   - `mapping/failure_to_patch_map.csv`를 근거로 `reports/patch_coverage.md`를 업데이트한다.
   - Stage 4 `reports/failure_cases.md`와 링크가 일치하는지 확인한다.

## 검토 체크리스트
- `reports/lint_report.md`에 용어·우선순위·링크 충돌이 0건으로 기록되었는가?
- `reports/audit_report.md`가 권고/경고를 보강 문서 섹션과 함께 제시하는가?
- `reports/patch_coverage.md`가 Stage 4 실패 항목의 ≥80%가 패치 문서로 해결 가능함을 수치로 증명하는가?
- 모든 스크립트가 데이터를 수정하지 않고 읽기만 수행하는지 코드 수준에서 확인했는가?

## 참고
- Stage 3 보강 문서(`../03_rule_refine/changes/*`)와 Stage 4 실패 기록(`../04_main_eval/reports/failure_cases.md`)을 교차 검토하여 링크가 정확한지 확인합니다.
- Surface rail, counter-current, emotion cloud 용어는 Stage 0 용어집과 Stage 3 폐쇄형 리스트를 그대로 사용합니다.

