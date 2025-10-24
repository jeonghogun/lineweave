# 대화 체인 및 리본 스케일 노트

Stage 4 failure cases #9, #10에서 발견된 다중 턴 연결 부족과 리본 값 중립화 문제를 해결하기 위한 가이드이다. Stage 1 `annotation_template.jsonl`과 Stage 0 `metrics.md`의 리본 축 정의를 따른다.

## 1. Chain linking
- `discourse_links`에 `chain_id` 필드를 추가 기재(데이터 수정은 추후 단계). 예: `chain_id: "turn_02"`.
- 동일 chain ID 내에서 `source_sentence`는 이전 턴, `target_sentence`는 다음 턴을 가리킨다.
- 3개 이상 턴이 연결되면 `notes`에 순서를 서술한다: "chain turn_02: A→B→C".
- Stage 4 `doc_025`의 세 턴 대화처럼 pairwise edge만 있는 경우, 감사 보고서에서 보강 필요 경고가 출력된다.

## 2. Ribbon micro-scale
- 대화 리본 값은 `-1`(설득 감퇴) ~ `+1`(설득 강화) 범위에서 0.25 단위까지 허용한다.
- 설득 시도가 명확히 존재하면 `±0.5` 이상을 부여하고, 완전 중립일 때만 `0`을 유지한다.
- 감정 구름이 `resolve` 또는 `critique`로 바뀌면 리본 값을 ±0.5 이상 조정한다.
- Stage 4 `doc_026` 사례처럼 자동 `0`이 부여된 경우, `notes`에 이유를 남기고 추후 재주석 시 수동 조정한다.

## 3. Review checklist
1. chain ID가 누락되었는가? → `audit_annotations.py`가 경고.
2. 리본 값이 0인데 설득 어휘("should", "must", "convince")가 있는가? → ±0.5로 조정 권고.
3. 대화 turn이 2개 이상인데 `discourse_links` 수가 turn-1보다 작은가? → `dialog_chain_notes.md`를 참조해 보완.
