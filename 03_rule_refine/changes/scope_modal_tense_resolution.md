# 모달 vs 시제 스코프 충돌 해소 규정

Stage 2 IAA 하락 원인이었던 모달·시제 우선순위 혼선을 제거하기 위해 다음 결정 트리와 예시를 확정합니다. 결정 트리는 `examples/scope_decision_tree.png`와 동일 구조를 갖습니다.

## 결정 트리 요약
1. **모달 의도 탐지**: "should", "must", "be allowed" 등 의무/가능/추측 모달이 존재하면 최상위 고리를 모달로 지정한다.
2. **모달 중첩 처리**: 모달이 두 개 이상일 경우 의무 > 가능 > 추측 > 약한 정동 순으로 상위에 배치한다.
3. **시제 판단**: 모달이 없다면 시제(과거/현재/미래)를 최상위로 둔다. 모달 다음에는 항상 시제를 둔다.
4. **상(Aspect)**: 완료·진행 표현은 시제 바로 아래에 배치하고, 시제가 없을 경우 모달 아래에 둔다.
5. **수식 요소**: 빈도/강조/부정/정도 등은 가장 하위 고리로 배치한다.
6. **보조 다리 활용**: 모달 해석이 우선이지만, 시간 정보를 잃지 않기 위해 보조 다리(`auxiliary bridge`)로 시제 노드를 재지정한다.

## 적용 예시
| 문장 | 해석 A (잘못된 판정) | 해석 B (규정 적용) | 근거 |
| --- | --- | --- | --- |
| "We should have finished the report." | `tense(past) > modal(should)` | `modal(should) > aspect(perfect have) > verb(finish)` | 의무 표현이 문장 핵심. 완료는 보조 다리로 과거 시점을 지지.
| "Citizens can vote tomorrow." | `tense(future) > modal(can)` | `modal(can) > tense(future) > verb(vote)` | 가능 모달이 정책 의도를 전달. 날짜는 보조 다리.
| "Managers must review and will update." | `tense(future) > modal(must)` | `modal(must) > tense(future) > coordination(review, update)` | 의무가 최상위. 미래 시제는 동일 레벨.
| "It was planned to allow visits." | `tense(past)` | `modal(allow) > tense(past was planned)` | 허용 의도(모달)가 핵심. 과거 시제는 계획의 맥락.
| "They might be working." | `aspect(progressive) > modal(might)` | `modal(might) > aspect(progressive be working)` | 추측 모달이 판단 근거. 진행 표현은 하위.
| "Guests were invited to stay." | `tense(past)` | `tense(past)` | 모달 부재 → 시제가 최상위. (반례: 규정으로 인해 변화 없음.)
| "Team leads may need to reconsider deadlines." | `tense(present)` | `modal(may) > modal(need) > verb(reconsider)` | 모달 두 개: 가능(may) vs 필요(need). 의무성 높은 need가 상위.
| "The policy will require employees to report weekly." | `tense(future)` | `modal(require) > tense(future will)` | 강제력 있는 require가 최상위, `will`은 시제.

## 실행 절차
1. 문장을 분해하여 모달/시제/상/수식 후보를 표기한다.
2. 표기한 후보를 결정 트리 순서대로 비교한다.
3. 우선순위와 예시 테이블을 참조하여 Stage 2에서 혼선이 난 경우(특히 doc_001, doc_002)의 판정을 재검증한다.
4. 결과를 주석 노트에 기록하고, 보조 다리 사용 여부를 명확히 기재한다.

이 문서와 PNG 트리는 동일 우선순위를 제공하며, 두 자료만으로 모달·시제 IAA 편차를 제거하도록 설계되었다.
