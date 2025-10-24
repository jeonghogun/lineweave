# 리뷰어 점검 체크리스트

각 문서를 검토할 때 아래 예/아니오 질문을 순서대로 확인하고, 하나라도 "아니오"면 수정 요청을 기록합니다.

1. 담화 태그
   - [ ] `discourse_links`의 각 항목이 `discourse_refinement.md`의 트리거 신호를 근거로 설명되는가?
   - [ ] `examples/discourse_negative_cases.md`에 열거된 반례가 반복되지 않았는가?

2. 스코프 고리
   - [ ] 모든 모달 문장이 결정 트리(`examples/scope_decision_tree.png`) 흐름대로 주석되었는가?
   - [ ] 보조 다리 사용 여부가 `notes`에 기록되었는가?

3. 반대 기류
   - [ ] 플래그가 있는 문장은 `counter_current_checks.md` 유형 중 하나로 명시되었는가?
   - [ ] 보존 의무 사항이 요약/생성 지침에 반영되었는가?

4. 감정 구름
   - [ ] 라벨이 `emotion_cloud_lexicon.md`의 8종 또는 `none`만 사용하는가?
   - [ ] 감정 변경이 담화 전환과 일치하는지 설명이 있는가?

5. Stage 2 연계
   - [ ] `02_pilot/reports/error_catalog.md`의 해당 오류 항목과 대응 문단이 주석 노트에 연결되었는가?
   - [ ] 새롭게 발견된 모호성이 있다면 Stage 4 계획에 기록되었는가?

모든 항목이 "예"일 때만 Gate G3 평가를 통과한 것으로 간주합니다.
