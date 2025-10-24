# Stage 1 메트릭 보강 정의

## Scope-Consistency
- 문장 및 문단 수준에서 스코프 고리의 우선순위, 범위, 겹침 해소가 규칙과 일치하는 정도.
- 측정 준비: 각 고리에 우선순위 태그와 적용 근거를 기록하여 비교 가능하도록 한다.

## Discourse-Edge Coverage
- 담화 점선이 요구되는 모든 문장 쌍을 포괄했는지 평가하는 지표.
- 측정 준비: `discourse_links`에 관계 태그, 근거 유형, 확신도를 표준화된 어휘로 기록한다.

## Coref-Confidence Calibration
- 명사·대명사 노드 간 지시 관계가 일관된 확신도로 표시되는지 검증.
- 측정 준비: 점선 또는 노트에 지시 근거와 불확실성 등급을 기재한다.

## Counter-Current Preservation Rate
- 반대 기류 플래그가 필요한 구간에서 실제로 부착되었는지, 요약·생성 시 보존되는지를 측정.
- 측정 준비: `counter_current_flags`에 유형, 범위, 근거를 필수 필드로 기록한다.

## Human Explainability Score
- 주석자가 규칙 적용 이유를 일관되게 설명할 수 있는지 평가하는 질적 항목.
- 측정 준비: 체크리스트의 근거 칸과 `notes` 필드를 사용해 결정 이유를 문장으로 남긴다.
