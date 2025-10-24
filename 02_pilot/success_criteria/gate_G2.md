# Gate G2 – 파일럿 합격 기준

1. **IAA 충족**
   - Scope-Consistency, Discourse-Edge Coverage, Counter-Current Preservation Rate의 매크로 평균 ≥ 0.80.
   - 축별 점수가 0.80 미만일 경우, `reports/error_catalog.md`에 개선 계획을 명시해야 하며 Stage 3에서 조치한다.
2. **스키마 유효성**
   - `scripts/validate_schema.py` 실행 시 필수 필드 누락 0건.
   - 특정 필드에 빈 배열을 기록할 경우 `validation_checks`에 검토 여부를 명시한다.
3. **오류 카탈로그 완비**
   - 치명 실패(규칙 위반으로 합의 불가)가 0건.
   - 경미 실패는 보류/재주석 계획을 `reports/error_catalog.md`에 서술한다.
4. **데이터 출처 투명성**
   - `data/sources.md`에 모든 문서의 출처, 장르, 라이선스 명시.
5. **프로토콜 추적성**
   - 독립 주석 → 충돌 기록 → 조정본이 `01_rules/protocols/annotation_protocol.md` 및 `adjudication_guidelines.md` 절차를 따른다는 근거를 `reports/iaa_pilot.md`/`reports/error_catalog.md`에서 확인할 수 있어야 한다.
