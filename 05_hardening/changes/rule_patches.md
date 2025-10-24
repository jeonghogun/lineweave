# Stage 5 규칙 패치 요약

Stage 4 `reports/failure_cases.md`의 12개 항목을 재정리하고, 각 항목을 보강한 Stage 5 문서와 Stage 3/4 원문 위치를 함께 명시한다. 모든 링크는 상대 경로이며 데이터 수정 없이 문서 업데이트만 수행한다.

| Failure ID | 요약 | 참조 원문 | Stage 5 패치 | 보강 포인트 |
| --- | --- | --- | --- | --- |
| 1 | `result` vs `elaboration` 동률 | [Stage 4 failure #1](../../04_main_eval/reports/failure_cases.md) | [discourse tie §1](./discourse_tie_breakers.md#1-result-vs-elaboration-lexical-cues) | 결과술어 유무·후행 서술어 기준으로 `result` 우선순위 명시 |
| 2 | 모달 vs 인과 경쟁 | [Stage 4 failure #2](../../04_main_eval/reports/failure_cases.md) | [causal modal §2](./causal_modal_edge_cases.md#2-deontic-vs-causal-branch) | 모달 신호 + 인과 표지 공존 시 분기 및 예시 제공 |
| 3 | 반대 기류 누락 | [Stage 4 failure #3](../../04_main_eval/reports/failure_cases.md) | [counter current §2](./counter_current_strength.md#2-soft-flag-retention-checklist) | adversative 접속부 유무에 따른 soft/strong 기록 강제 |
| 4 | 증거 스팬 과소 | [Stage 4 failure #4](../../04_main_eval/reports/failure_cases.md) | [evidence span §1](./evidence_span_guidelines.md#1-clause-granularity) | 절 단위 인용과 스코프링 ID 병기 절차 명시 |
| 5 | 질문형 전환 혼선 | [Stage 4 failure #5](../../04_main_eval/reports/failure_cases.md) | [question quote §1](./question_quote_rules.md#1-question-led-transitions) | 질문 문장과 전환 태그 구분 규칙 + 대화 예시 |
| 6 | 감정 구름 중립 경계 | [Stage 4 failure #6](../../04_main_eval/reports/failure_cases.md) | [question quote §2](./question_quote_rules.md#2-emotion-cloud-defaults) | `calm` 디폴트 신호어·hedging 기준 강화 |
| 7 | 스코프 범위 클리핑 | [Stage 4 failure #7](../../04_main_eval/reports/failure_cases.md) | [question quote §3](./question_quote_rules.md#3-quote-boundary-scope) | 인용부호 포함 범위 및 punctuation 규칙 재강조 |
| 8 | 반대 기류 강도 미정 | [Stage 4 failure #8](../../04_main_eval/reports/failure_cases.md) | [counter current §1](./counter_current_strength.md#1-strength-layers) | soft/strong 층화와 보존 조건 도입 |
| 9 | 대화 체인 제한 | [Stage 4 failure #9](../../04_main_eval/reports/failure_cases.md) | [dialog chain §1](./dialog_chain_notes.md#1-chain-linking) | turn-id 사슬 표기 규격 제시 |
| 10 | 리본 중립값 남용 | [Stage 4 failure #10](../../04_main_eval/reports/failure_cases.md) | [dialog chain §2](./dialog_chain_notes.md#2-ribbon-micro-scale) | 대화 리본 스케일 가이드와 persuasion ±1 예시 |
| 11 | `because` 혼합 태그 | [Stage 4 failure #11](../../04_main_eval/reports/failure_cases.md) | [discourse tie §2](./discourse_tie_breakers.md#2-because-dominance) | because 절이 있을 때 `cause` 우선 규칙 확정 |
| 12 | Surface rail 기록 피로 | [Stage 4 failure #12](../../04_main_eval/reports/failure_cases.md) | [surface rail §2](./surface_rail_macros.md#2-macro-prompt-structure) | 매크로 기반 note 템플릿 명세와 요약 슬롯 지정 |

각 Stage 5 문서는 Stage 3 변경 사항과 0–4단계 용어 정의를 그대로 차용하며, 추가된 규정은 Stage 6 이후 재주석 시 그대로 적용 가능하도록 작성하였다.
