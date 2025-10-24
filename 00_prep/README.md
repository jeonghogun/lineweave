# 0단계 준비 지침

## 폴더 구조 개요
```
00_prep/
  README.md
  glossary/
    glossary.md
  diagrams/
    lode_overview.mmd
    lode_overview.png
    puppeteer-config.json
  success_criteria/
    gate_G0.md
    metrics.md
  scripts/
    export_diagram.sh
```

## Mermaid 렌더러 설치
1. Node.js 18 이상이 설치되어 있는지 확인합니다 (`node -v`).
2. Mermaid CLI를 전역 설치합니다.
   ```bash
   npm install -g @mermaid-js/mermaid-cli
   ```
3. Linux 환경에서 루트 사용자로 실행하는 경우 추가로 필요한 라이브러리를 설치합니다.
   ```bash
   sudo apt-get update
   sudo apt-get install -y libatk-bridge2.0-0 libgtk-3-0 libnss3 libx11-xcb1 \
     libxcomposite1 libxcursor1 libxdamage1 libxi6 libxrandr2 libgbm1 \
     libpango-1.0-0 libpangocairo-1.0-0 libatspi2.0-0 libcups2 libdrm2 \
     libxkbcommon0 libxshmfence1 libasound2t64
   ```

## 도식 내보내기 스크립트 실행
1. 저장소 루트에서 스크립트를 실행합니다.
   ```bash
   00_prep/scripts/export_diagram.sh
   ```
2. 성공 시 `diagrams/lode_overview.png`가 새로 생성·갱신되며, "Diagram exported" 메시지가 출력됩니다.
3. 실패 시 Mermaid CLI 설치 여부 또는 Puppeteer 구성(`diagrams/puppeteer-config.json`)을 확인합니다.

## 폴더 점검 체크리스트
- `glossary/glossary.md`에 12개 용어의 정의·역할·경계가 모두 포함되어 있는가?
- `diagrams/` 폴더에 `.mmd`, `.png`, `puppeteer-config.json` 파일이 존재하는가?
- `success_criteria/` 폴더에 `gate_G0.md`, `metrics.md`가 존재하며 상호 참조하는가?
- `scripts/export_diagram.sh`가 실행 권한을 가지고 있는가?

## 시각 검토 포인트
- 도식에 직선, 모음, 고리, 구름, 점선, 면, 페이지 기류, 반대 기류 보존, 캡슐, 보조 다리, 형태 레일이 모두 나타나는가?
- 범례의 기호와 색이 glossary 및 성공 기준 문서와 일치하는가?
- 캡슐과 보조 다리가 직선을 적절히 연결하고 반대 기류 표기가 페이지 기류와 구분되는가?
