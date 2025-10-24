# 3단계 규칙 보강 개요

## 목적
Stage 2 파일럿에서 드러난 담화 태그 편차, 모달·시제 스코프 혼선, 반대 기류 유형 불일치, 감정 구름 명칭 혼재를 문서화로 보강하여 재주석 없이도 일관된 해석을 확보합니다.

## 폴더 구성
- `changes/`: 담화·스코프·반대 기류·감정 구름 보강 문서
- `examples/`: 담화 태깅 정오 사례와 스코프 결정 트리 이미지
- `checklists/`: 조정 및 리뷰어용 빠른 점검표
- `success_criteria/`: Gate G3 합격 기준

## 로컬 작업 지시
1. **도식 렌더링**: `examples/scope_decision_tree.png`는 Pillow로 생성된 결정 트리 이미지입니다. 필요 시 다음 명령으로 재생성하세요.
   ```bash
   cd 03_rule_refine
   python ../tools/render_scope_tree.py
   ```
   (스크립트는 `tools/render_scope_tree.py`에 위치하며, PNG만 갱신하고 다른 파일을 만들지 않습니다.)
   - Pillow가 설치되어 있지 않다면 `pip install pillow` 후 실행합니다.
2. **보강 문서 검수 순서**:
   1. `changes/discourse_refinement.md`와 `examples/discourse_positive_cases.md`·`discourse_negative_cases.md`를 대조하며 담화 태그 구분을 확인합니다.
   2. `changes/scope_modal_tense_resolution.md`와 `examples/scope_decision_tree.png`를 참고하여 스코프 해석 충돌을 점검합니다.
   3. `changes/counter_current_checks.md`의 체크리스트를 따라 반대 기류 유지 의무를 검토합니다.
   4. `changes/emotion_cloud_lexicon.md`를 활용해 감정 구름 용어가 폐쇄형 리스트 내에서 사용되었는지 확인합니다.
3. **링크 맵 작성**: 2단계 `reports/error_catalog.md`를 열어 각 오류 유형을 `changes/`와 `examples/` 문서의 대응 절로 연결하는 표를 작성하고, Stage 4 준비 메모에 포함합니다.

## 체크리스트
- [ ] 담화·스코프·반대 기류·감정 구름 문서가 Stage 1 용어와 일치하는가?
- [ ] `scope_decision_tree.png`가 결정 트리 본문과 동일한 경로/우선순위를 시각화하는가?
- [ ] 예시 20건(정/오 사례 각 10건 이상)이 모두 근거 문장과 설명을 포함하는가?
- [ ] Gate G3 기준이 문서 간 모순 방지와 기대 IAA 개선 근거를 모두 명시하는가?

## 참고
- Stage 2 파일럿 리포트: `02_pilot/reports/`
- Stage 1 규칙서: `01_rules/guidelines/`

