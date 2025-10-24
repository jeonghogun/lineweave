# 02_pilot: 파일럿 주석 & IAA 검증

## 단계 목표
- 01_rules에서 확정한 직선·모음·고리·점선·반대 기류·캡슐·보조 다리 규칙을 실제 텍스트에 적용한다.
- 두 명의 독립 주석자(A, B)가 6개 문서를 주석하고, 조정본을 작성한다.
- Scope-Consistency / Discourse-Edge Coverage / Counter-Current Preservation Rate에 대해 IAA ≥ 0.80을 달성했는지 확인한다.

## 폴더 구성
- `data/raw/` : 뉴스·논설·대화 장르별 실제 텍스트 6편(프로젝트 작성, CC BY 4.0 공개).
- `annotations/` : annotator_A.jsonl, annotator_B.jsonl, adjudication 결과 agreed.jsonl.
- `scripts/` : 템플릿 필수 필드 검증(`validate_schema.py`), IAA 산출(`compute_iaa.py`).
- `reports/` : IAA 결과 요약(`iaa_pilot.md`), 충돌 원인 기록(`error_catalog.md`).
- `success_criteria/` : Gate G2 규정.

## 로컬 작업 지시
1. **데이터 수집/검수**
   - 외부 텍스트 추가 시 라이선스·출처를 `data/sources.md`에 즉시 기록.
   - 개인정보·민감정보가 발견되면 해당 문서를 제외하거나 수정 후 이유를 기록.
2. **스키마 검증**
   - `python scripts/validate_schema.py annotations/annotator_A.jsonl annotations/annotator_B.jsonl annotations/agreed.jsonl`
   - 스크립트는 필드 존재 여부만 확인하며 파일을 수정/생성하지 않는다.
3. **IAA 계산**
   - `python scripts/compute_iaa.py annotations/annotator_A.jsonl annotations/annotator_B.jsonl`
   - 출력된 축별 평균과 전체 평균을 `reports/iaa_pilot.md` 표에 반영.
4. **조정 절차 재현**
   - `01_rules/protocols/annotation_protocol.md`와 `adjudication_guidelines.md`에 따라 합의본을 유지.
5. **수작업 점검 체크리스트**
   - 스코프 우선순위 기록이 Stage 1 규칙과 상충하지 않는지 확인.
   - 담화 관계 태그가 `guidelines/discourse_inventory.md`의 정의와 일치하는지 재검토.
   - `counter_current_flags`가 모두 근거 문장을 명시하는지 확인.
   - 캡슐/보조 다리 표기가 Stage 0/1 용어와 동일한지 확인.

## 작업 금지 사항
- 더미 텍스트 또는 무근거 수치 삽입 금지.
- 스크립트는 파일 생성/수정 기능을 포함하지 않는다.
- IAA 목표를 맞추기 위해 주석 규칙을 사후 변경하지 않는다.

## 검토 포인트
- 장르별 최소 2편씩 존재하는지 (`data/raw/doc_001`~`doc_006`).
- 각 주석 파일에 필수 필드가 모두 포함되어 있는지.
- `reports/error_catalog.md`에 모든 충돌 유형과 참조 규칙 링크가 기재되어 있는지.
- Gate G2 조건 충족 여부를 `reports/iaa_pilot.md`에서 명확히 명시했는지.

## 후속 단계 준비
- 남은 모호성은 `reports/error_catalog.md`에 기록하고 03단계에서 규칙 보강 계획으로 연결한다.
