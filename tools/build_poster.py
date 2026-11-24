#!/usr/bin/env python3
"""Build the news poster for make.fun news-image-20261124.

Draws a 1024x1024 newspaper-style poster in PIL:
  masthead with the date -> AI-illustrated hero band -> 6-story grid -> footer.
Text is rendered with PIL (crisp, no AI-garbled text); the hero illustration
(assets/hero.webp) was generated with an image model with a no-text prompt.
Output: ../entry.png (PNG, <= 1 MiB, <= 1024x1024).
"""
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
HERO = ROOT / "assets" / "media-generation-hero-0-30e9ccbe-be5c-434d-b6e7-293b874918a6.webp"
OUT = ROOT / "entry.png"

W, H = 1024, 1024
NAVY = (16, 28, 78)
AMBER = (232, 160, 32)
PAPER = (247, 243, 232)
INK = (20, 20, 20)
GREY = (90, 90, 90)
DIVIDER = (216, 210, 192)


def font(bold: bool, size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont,
         max_w: int) -> list[str]:
    """Greedy word wrap to max_w pixels."""
    lines: list[str] = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for word in words:
            trial = f"{cur} {word}".strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    return lines


STORIES = [
    ("MARKETS", (176, 92, 8),
     "NVIDIA BRINGS BACK HUANG",
     "Huang returns as CEO after resigning on 12 Nov; Trump says he \u201cmade the deal\u201d. Nasdaq +6.5%."),
    ("CLIMATE", (31, 120, 76),
     "CLIMATE TALKS COLLAPSE",
     "COP31 ends with no deal as the EU rejects the final text from Turkey and Australia."),
    ("WAR", (140, 32, 32),
     "UKRAINE DRONES HIT RUSSIAN SHIPS",
     "Two Russian ships struck off Libya on Sunday; Russian strikes kill 12 in Kyiv region."),
    ("BRITAIN", (16, 70, 130),
     "12,000 EVACUATED IN MANCHESTER",
     "Concert at Manchester\u2019s Co-op Live cleared after an unknown substance is released."),
    ("RIGHTS", (110, 52, 130),
     "IRAN FLOGS SINGER 74 LASHES",
     "Parastoo Ahmadi and four crew members each receive 74 lashes for a concert without hijab."),
    ("DISASTER", (120, 74, 10),
     "24 KILLED IN INDONESIA FACTORY FIRE",
     "Blaze at a sweet factory kills 24; dozens still missing as rescuers search the site."),
]


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 132], fill=NAVY)
    title_f = font(True, 56)
    d.text((W // 2, 16), "THE WORLD IN ONE DAY", font=title_f, fill="white",
           anchor="ma")
    date_f = font(True, 30)
    d.text((W // 2, 82), "TUESDAY, 24 NOVEMBER 2026", font=date_f, fill=AMBER,
           anchor="ma")
    d.rectangle([0, 130, W, 134], fill=AMBER)

    # --- hero band (132..500) ---
    hero = Image.open(HERO).convert("RGB")
    hw, hh = hero.size
    target_w, target_h = W, 368
    scale = max(target_w / hw, target_h / hh)
    hero = hero.resize((round(hw * scale), round(hh * scale)), Image.LANCZOS)
    x0 = (hero.width - target_w) // 2
    y0 = (hero.height - target_h) // 2
    img.paste(hero.crop((x0, y0, x0 + target_w, y0 + target_h)), (0, 134))

    # --- story grid (502..972): 2 cols x 3 rows ---
    grid_top, grid_bottom = 502, 972
    col_w, row_h = W // 2, (grid_bottom - grid_top) // 3
    for i, (tag, colour, headline, summary) in enumerate(STORIES):
        col, row = i % 2, i // 2
        cx, cy = col * col_w, grid_top + row * row_h
        # dividers
        if col == 1:
            d.line([col_w, cy, col_w, cy + row_h], fill=DIVIDER, width=2)
        if row > 0:
            d.line([0, cy, W, cy], fill=DIVIDER, width=2)
        px, py = cx + 18, cy + 14
        # tag chip
        tag_f = font(True, 16)
        tw = d.textlength(tag, font=tag_f)
        d.rounded_rectangle([px, py, px + tw + 18, py + 26], radius=4, fill=colour)
        d.text((px + 9, py + 4), tag, font=tag_f, fill="white")
        # headline (up to 2 lines)
        hl_f = font(True, 23)
        hl_lines = wrap(d, headline, hl_f, col_w - 36)[:2]
        hy = py + 36
        for line in hl_lines:
            d.text((px, hy), line, font=hl_f, fill=INK)
            hy += 28
        # summary (up to 2 lines)
        sm_f = font(False, 18)
        sm_lines = wrap(d, summary, sm_f, col_w - 36)[:2]
        sy = hy + 4
        for line in sm_lines:
            d.text((px, sy), line, font=sm_f, fill=(60, 60, 60))
            sy += 23

    # --- footer ---
    d.rectangle([0, 972, W, H], fill=NAVY)
    ft_f = font(False, 16)
    d.text((W // 2, 990),
           "24 NOVEMBER 2026  \u2022  As reported by Reuters and the BBC  "
           "\u2022  make.fun news-image-20261124",
           font=ft_f, fill="white", anchor="ma")

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {img.size} {OUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
