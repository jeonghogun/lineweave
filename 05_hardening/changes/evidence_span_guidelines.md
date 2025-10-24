# 증거 스팬 세분화 지침

Stage 4 failure case #4에서 제기된 "evidence" 필드의 단편적 인용 문제를 해결하기 위해 Stage 1 `annotation_template.jsonl` 구조를 보완 설명한다. 데이터는 수정하지 않고 표기 규칙만 고정한다.

## 1. Clause granularity
- `discourse_links.evidence`에는 최소 한 개의 절(clause)을 완전 인용한다.
- 절 인용 시 시작·끝 토큰을 `tokens[start:end]` 형식으로 명시하고, 80자 이상 확보를 권장한다.
- 절이 길 경우 `…` 생략 기호를 사용하되, 원인/결과 구문은 생략하지 않는다.

## 2. Scope ring references
- 관련 범위가 명확할 때 `scope_rings` ID를 병기한다: 예) `S1: tokens[0:45] → S2: tokens[46:90]`.
- 인용부에 고리가 없으면 `scope:none`을 명시해 추후 보강 필요성을 드러낸다.
- Stage 1 `scope_priority.md` 우선순위(`부정 → 모달 → 시제≈상 → 수식`)를 반복 표기하여 검토자가 재확인하도록 한다.

## 3. Evidence note template
```
Evidence: tokens[12:40] "because the militia had scattered" (S1 cause) → tokens[41:72] "so the council delayed" (S2 result)
Notes: Stage5 evidence span guideline applied – clause-level quote + ring IDs.
```
- Stage 4 `doc_018` 사례처럼 세부 묘사를 요구할 때, 위 템플릿만 추가하면 재주석 없이도 근거가 보강된다.
- 감사 스크립트는 evidence 길이가 60자 미만이거나 스코프 ID가 없으면 권고 메시지를 출력하도록 설정하였다.
