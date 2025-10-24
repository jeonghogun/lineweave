# 모달·인과 경계 분기 규칙

Stage 3 [`scope_modal_tense_resolution.md`](../../03_rule_refine/changes/scope_modal_tense_resolution.md)의 결정 트리를 확장하여 Stage 4 failure case #2에서 나타난 모달/인과 충돌을 해소한다. 기본 우선순위 `부정 → 모달 → 시제≈상 → 수식`(Stage 1 `scope_priority.md`)은 그대로 유지한다.

## 1. 결정 트리 요약
1. **부정 확인**: 문장에 부정사(`not`, `never`, `없다`)가 있으면 부정 고리를 최우선 적용하고, 이하 단계에서 같은 범위를 공유한다.
2. **모달 분기**: `should`, `must`, `can`, `ought`, `may`, `need` 등 의무/가능 표시가 있으면 모달 고리를 배치한다.
3. **인과 표지 검사**: 모달이 존재하더라도 `because`, `so that`, `따라서` 등 인과 신호가 있으면 모달 고리 내부에 인과 점선을 연결한다.
4. **시제·상 보정**: 명시적 시간 지시어가 있으면 시제/상 고리를 모달 안쪽에 중첩한다.
5. **수식 요소 배치**: 강조/조건 부사구는 가장 안쪽에서 처리한다.

## 2. Deontic vs causal branch
- **Case A – 의무 + 인과**: "We must act because the threat is imminent." → 모달 고리가 외곽, 인과 점선은 `cause`로 지정.
- **Case B – 가능성 + 결과 설명**: "The alliance can fail if supply breaks." → 모달(`can`) 고리를 우선, 조건/인과 점선을 내부에 둔다.
- **Case C – 의무만 존재**: 인과 신호가 없으면 Stage 3 규칙 그대로 모달만 유지한다.
- **예외 처리**: 인과 표지가 가정법(`if we must`)을 형성하면 `condition`을 우선으로 기록하고 인과는 보류한다.

## 3. Worked examples
1. **Federalist No. 4** (Stage 4 doc_014): "We must remain armed because rivals grow bold." → `S1` 모달, `D1` `cause`.
2. **Policy brief**: "Leaders should reconsider, for the market has shifted." → `should` 모달, `for`는 인과로 간주하여 `result` 적용.
3. **Dialogue snippet**: "Can we go since the storm clears?" → 질문형이지만 모달 `can`을 유지하고, `since` 신호로 `result` 대신 `cause`를 부여.
4. **Counter example**: "We must act if the report is true." → `if`가 조건을 형성하므로 `condition`이 우선, 인과 점선 미부여.

각 예시는 Stage 4 `failure_cases.md` #2, #11에 대응하며, 인용 시 Stage 1 템플릿의 `scope_rings` 레이블을 그대로 사용한다.
