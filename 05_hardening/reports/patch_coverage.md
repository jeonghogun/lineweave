# Stage 5 Patch Coverage Summary

| 항목 | 값 |
| --- | --- |
| Stage 4 failure cases 총수 | 12 |
| Stage 5 문서로 직접 커버한 항목 | 12 |
| 커버리지 비율 | 100% |

## 근거
- `mapping/failure_to_patch_map.csv`에서 failure_id 1–12가 각각 최소 1개의 Stage 5 패치 섹션으로 매핑됨을 확인했다.
- 각 매핑 항목은 Stage 4 `reports/failure_cases.md`의 원문 링크와 Stage 5 보강 문서 링크를 동시에 제공하여 추적성을 확보한다.
- 감사 스크립트 `audit_annotations.py`는 패치 문서에서 요구하는 신호(예: "Surface rail audit:" 매크로, `strength:` 메모)를 찾지 못하면 권고 메시지를 출력해 보강 필요성을 보여준다.

## Stage 3/4 연계
- 담화 동률 관련 항목(#1, #11)은 Stage 3 `discourse_refinement.md` 우선순위를 반복 확인하도록 작성되었다.
- 모달/인과 충돌(#2)은 Stage 3 결정 트리를 유지하면서 추가 분기를 정의했다.
- Surface rail과 리본 보정(#10, #12)은 Stage 0 metric 축 정의와 Stage 3 reviewer 체크리스트를 그대로 참고한다.

이로써 failure case의 100%가 Stage 5 문서만으로 대응 가능함을 문서화했다.
