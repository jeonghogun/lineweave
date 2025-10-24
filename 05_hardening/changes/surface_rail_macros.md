# Surface Rail 보조 매크로 명세

Stage 4 failure case #12에서 제기된 `surface_rail_notes` 피로 문제를 해결하기 위해, Stage 3 `adjudication_quickref.md`와 연동 가능한 문서 템플릿을 정의한다. 자동화 코드는 작성하지 않고, 텍스트 규격만 고정한다.

## 1. Macro objective
- Stage 3 `reviewer_audit.md` 체크 항목을 요약해 annotator가 빠르게 복사할 수 있는 문구를 제공한다.
- Surface rail 라벨(`line`, `operator`, `ring`, `cloud`, `counter`)을 세트로 묶어 단일 문장에 기록한다.
- 매크로는 문서 편집기 단축키 또는 스니펫 툴에서 사용할 수 있도록 작성한다.

## 2. Macro prompt structure
```
Surface rail audit:
- line focus: <capsule/ribbon alignment>
- operator shift: <operator summary>
- ring/ribbon delta: <value with ±0.25 increments>
- cloud tone: <Stage3 lexicon label>
- counter-current flag: <soft|strong|none>
Deviation note: <free text>
```
- `<Stage3 lexicon label>`에는 `calm`, `concern`, `alarm`, `joy`, `resolve`, `regret`, `hope`, `critique`만 허용한다.
- `counter-current flag` 값은 `counter_current_strength.md`에서 정의한 soft/strong을 따른다.
- `Deviation note`는 120자 이내로 요약하고, 추가 설명이 필요하면 `notes` 필드에 이어서 작성한다.

## 3. Usage checklist
1. 매크로 적용 여부를 `validation_checks.surface_rail_macro_used: true/false`로 기록(추가 필드 필요 시 Stage 6에서 확정).
2. Surface rail 값이 0일 때도 매크로를 입력하여 중립 근거를 명시한다.
3. 감사 스크립트는 매크로 키워드(`Surface rail audit:`) 부재 시 권고 메시지를 출력한다.
