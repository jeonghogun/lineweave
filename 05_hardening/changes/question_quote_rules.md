# 질문/인용 스코프 규칙

Stage 4 failure cases #5, #6, #7에서 발견된 질문형 전환 혼선, 감정 구름 경계, 인용부 범위 문제를 해결하기 위한 세부 규정이다. Stage 3 [`discourse_refinement.md`](../../03_rule_refine/changes/discourse_refinement.md)와 [`emotion_cloud_lexicon.md`](../../03_rule_refine/changes/emotion_cloud_lexicon.md)를 준수한다.

## 1. Question-led transitions
- 문장이 질문 형태(`?`)라 하더라도 **정보 전달 목적**이면 `전환` 또는 `전개` 태그를 우선 고려한다.
- 실제 질문-응답 구조인지 확인하기 위해 다음 신호를 사용한다:
  - 화자 지시(`he asked`, "그가 물었다")가 있으면 `메타발화`.
  - 후속 문장이 답변이라면 `discourse_links`에 `result` 대신 `transition`을 기록한다.
- Stage 4 `doc_021` 유형에 대해, 질문형 문장을 `transition`으로 표기할 때 `notes`에 "question-led transition" 문구를 남긴다.

## 2. Emotion cloud defaults
- 감정 구름 라벨이 비워져 있고 hedging 동사("might", "perhaps", "seems")가 존재하면 `calm`을 기본값으로 사용한다.
- 반대로 위험 신호(`warn`, "우려", "concerned")가 존재하면 `concern`으로 전환한다.
- 감정 구름 변경 시 `counter_current_strength.md`의 `soft/strong` 분류와 연결해 기록한다.

## 3. Quote boundary scope
- 직접 인용부호(`""`, `''`)가 포함되면, `scope_rings.span.end`가 닫는 인용부 직후 토큰까지 포함했는지 확인한다.
- 인용 안에서 담화 태그가 발생하면 `discourse_links.evidence`에 인용부를 그대로 인용하고 `scope`를 병기한다.
- Stage 4 `doc_007`, `doc_023` 사례처럼 따옴표 누락이 발생하면, `notes`에 "quote boundary extended"를 기록하여 검토자가 확인할 수 있게 한다.
