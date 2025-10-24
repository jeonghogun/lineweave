#!/usr/bin/env python3
"""Generate the modal-vs-tense scope decision tree PNG."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "03_rule_refine" / "examples" / "scope_decision_tree.png"

WIDTH, HEIGHT = 1400, 900
BACKGROUND = (255, 255, 255)
TEXT_COLOR = (33, 37, 41)
ACCENT = (64, 120, 192)
SECONDARY = (102, 187, 106)
BORDER = (33, 37, 41)
FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def load_fonts():
    regular = bold = None
    for path in FONT_PATHS:
        p = Path(path)
        if p.exists():
            if "Bold" in p.name:
                bold = ImageFont.truetype(str(p), 28)
            else:
                regular = ImageFont.truetype(str(p), 24)
    if regular is None:
        regular = ImageFont.load_default()
    if bold is None:
        bold = regular
    return regular, bold


def draw_box(draw, xy, text, font, fill):
    draw.rounded_rectangle(xy, radius=18, fill=fill, outline=BORDER, width=3)
    x0, y0, x1, y1 = xy
    bbox = draw.multiline_textbbox((0, 0), text, font=font, align="center")
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    draw.multiline_text(
        (x0 + (x1 - x0 - text_w) / 2, y0 + (y1 - y0 - text_h) / 2),
        text,
        font=font,
        fill=TEXT_COLOR,
        align="center",
    )


def draw_arrow(draw, start, end):
    draw.line([start, end], fill=BORDER, width=4)
    # simple triangular head
    arrow_size = 18
    direction = (end[0] - start[0], end[1] - start[1])
    length = (direction[0] ** 2 + direction[1] ** 2) ** 0.5
    if length == 0:
        return
    unit = (direction[0] / length, direction[1] / length)
    left = (
        end[0] - arrow_size * unit[0] + arrow_size * (-unit[1]),
        end[1] - arrow_size * unit[1] + arrow_size * unit[0],
    )
    right = (
        end[0] - arrow_size * unit[0] - arrow_size * (-unit[1]),
        end[1] - arrow_size * unit[1] - arrow_size * unit[0],
    )
    draw.polygon([end, left, right], fill=BORDER)


def main():
    regular, bold = load_fonts()
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)

    title_font = ImageFont.truetype(FONT_PATHS[0], 40) if Path(FONT_PATHS[0]).exists() else bold
    draw.text((WIDTH / 2, 40), "모달 vs 시제 스코프 결정 트리", fill=TEXT_COLOR, font=title_font, anchor="ma")

    root_box = (520, 110, 880, 210)
    draw_box(draw, root_box, "문장에 모달 의도 표현이 있는가?", bold, fill=(220, 235, 252))

    modal_yes = (220, 270, 580, 370)
    modal_no = (920, 270, 1280, 370)
    draw_box(draw, modal_yes, "예: can, should, be allowed\n→ 모달 고리를 최상위로", regular, fill=(222, 245, 234))
    draw_box(draw, modal_no, "아니오 → 시제/상 평가로 이동", regular, fill=(252, 240, 220))

    draw_arrow(draw, (700, 210), (400, 270))
    draw_arrow(draw, (700, 210), (1100, 270))

    modal_conflict = (220, 430, 580, 530)
    draw_box(draw, modal_conflict, "모달이 두 개 이상이면?\n→ 의무 > 가능 > 추측 순", regular, fill=(222, 245, 234))
    draw_arrow(draw, (400, 370), (400, 430))

    tense_box = (920, 430, 1280, 530)
    draw_box(draw, tense_box, "시제 표현 파악: 과거/현재/미래?\n→ 시제 고리 배치", regular, fill=(252, 240, 220))
    draw_arrow(draw, (1100, 370), (1100, 430))

    aspect_box = (920, 590, 1280, 690)
    draw_box(draw, aspect_box, "진행·완료(상)가 있으면 시제 바로 아래에", regular, fill=(252, 240, 220))
    draw_arrow(draw, (1100, 530), (1100, 590))

    modifier_box = (920, 750, 1280, 850)
    draw_box(draw, modifier_box, "수식 요소(빈도/강조)는 최하단", regular, fill=(252, 240, 220))
    draw_arrow(draw, (1100, 690), (1100, 750))

    conflict_note = (220, 590, 580, 730)
    draw_box(draw, conflict_note, "모달·시제 충돌 시:\n1) 진술 의도(모달) 우선\n2) 시간 해석은 보조 다리로 연결\n3) 예시: "
             "‘should have finished’ → should > have+finished", regular, fill=(255, 255, 245))
    draw_arrow(draw, (400, 530), (400, 590))

    image.save(OUTPUT)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
