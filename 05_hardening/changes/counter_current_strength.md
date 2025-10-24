# 반대 기류 강도 층화 지침

Stage 3 [`counter_current_checks.md`](../../03_rule_refine/changes/counter_current_checks.md)의 유형 정의를 확장하여 Stage 4 failure cases #3, #8에서 요구된 강도 구분과 기록 의무를 명문화한다.

## 1. Strength layers
| 강도 | 정의 | 적용 유형 | 보존 의무 |
| --- | --- | --- | --- |
| **soft** | 주 문장의 주장에 가벼운 보류·단서가 붙는 경우. | 반례 제시, 조건부 반박, 정서 반기류 | 요약 시 플래그 유지 + 1문장 요약에 단서 포함 |
| **strong** | 주장을 정면으로 부정하거나 대안을 제시하는 경우. | 역설, 대안 제시, 반박 연계 | 요약/생성에서 해당 문장 삭제 금지, 대안 키워드 유지 |

- 감정 구름 변화가 동반되면 `emotion_cloud_lexicon.md`의 8개 라벨 중 하나를 반드시 기록한다.
- `counter_current_flags` 항목의 `notes`에 `strength: soft|strong`을 추가 기재한다(데이터 수정은 Stage 6에서 적용, Stage 5에서는 지침만 고정).

## 2. Soft flag retention checklist
1. adversative 접속사("but", "그러나")가 존재하는가? → 존재하면 최소 `soft`로 유지.
2. 반례가 특정 범위(예: "소규모 지역")에 한정되는가? → `soft`로 분류하되 범위 기록.
3. 감정 구름이 완전히 반전되는가? → `strong` 후보 검토.
4. 플래그 생략을 요청하는 경우, `notes`에 누락 사유와 참조 규정을 반드시 남긴다.

## 3. Severity logging template
```
Counter-current: alternative current → strength: strong → rationale: proposes phased rollout (see Stage3 counter_current_checks §유형 정의)
```
- Stage 4 failure #3 (`doc_015`)와 #8 (`doc_024`)는 위 템플릿을 통해 재주석 없이도 검토 의견을 명시할 수 있다.
- 요약/생성 시 `soft`는 완화 표현 유지, `strong`은 내용 삭제 금지 항목으로 분류한다.
