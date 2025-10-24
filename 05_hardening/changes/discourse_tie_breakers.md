# 담화 동률 해소 규칙

Stage 3 [`discourse_refinement.md`](../../03_rule_refine/changes/discourse_refinement.md)에서 정의한 우선순위를 유지하되, Stage 4 failure cases #1, #5, #11에서 드러난 동률 상황을 해소하기 위한 근거 신호를 추가한다. 모든 태그 이름은 Stage 1 `discourse_inventory.md` 용어를 따른다.

## 1. result vs elaboration lexical cues
- **우선 순위**: Stage 3 우선순위(`반박 > 대조 > 전환 > 인과/결과 > 상세화/예시 > 전개 > 요약`)를 그대로 적용하되, `result`는 `elaboration`보다 항상 선순위에 둔다.
- **판단 절차**
  1. 후행 문장에 결과 술어(예: "leads to", "결과적으로", "따라서")가 있는지 확인한다.
  2. 선행 문장에 원인·조건 술어(예: "because", "due to", "원인", "때문")가 존재하면 `result`를 선택한다.
  3. 위 신호가 없고, 후행 문장이 세부 묘사 또는 통계 확장을 제공하면 `elaboration`으로 기록한다.
- **근거 기록**: `discourse_links.evidence`에는 원인/결과 표현을 그대로 인용하고, `notes`에 선택 근거를 한 줄 요약한다.

## 2. because dominance
- **적용 범위**: 문장 내 "because", "since", "왜냐하면" 등 인과 표지가 존재하나, 후행 설명이 서술적 열거인 경우.
- **규칙**
  1. 인과 표지가 명시되면, 결과 문장인지 여부와 관계없이 `cause` 또는 `result` 중 하나를 부여한다.
  2. 후행 문장에 새로운 원인 없이 기존 사실을 재진술하는 경우 `cause`를 우선 적용한다.
  3. 만약 후행 문장이 단순 예시라면, `cause` 태그를 유지하면서 `notes`에 예시임을 표기한다.
- **반례 처리**: 인과 표지가 조건절(예: "because if")로 전환되면, Stage 3 `condition` 규칙을 호출하고 `cause`를 보류한다.

## 3. 동률 해소 프로토콜
- **Step 1 – 신호어 검증**: `result`/`elaboration` 후보가 동시에 보이면 `result`를 우선 검토한다.
- **Step 2 – 접속사 확인**: `because`, `so that`, `따라서`가 존재하면 `cause/result` 선순위로 결정한다.
- **Step 3 – 감정 구름 확인**: 감정 구름이 변하면 `전환` 혹은 `반박` 후보를 재확인한다.
- **Step 4 – Stage 3 우선순위 재확인**: `반박 > 대조 > 전환 > 인과/결과 > 상세화/예시 > 전개 > 요약` 순서가 지켜졌는지 확인한다.
- **기록 요구**: 결정 과정이 애매했다면 `validation_checks.tie_breaker_reviewed` 플래그를 새로 추가하지 않고, `notes`에 "Stage5 tie-breaker consulted" 문구를 남긴다.

본 규칙은 Stage 4 `failure_cases.md`의 #1, #11 사례에 즉시 적용할 수 있으며, 질문형 전환 혼선(#5)은 `question_quote_rules.md`와 병행해 해결한다.
