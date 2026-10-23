"""Render a paper heading and a display thumbnail; preserve original sources."""
from pathlib import Path
import json
import fitz
import mpmath as mp
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
IMAGES = ROOT / "04_第四篇_AI新纪元" / "img"
SOURCES = ROOT / "资料" / "16_Claude的核弹" / "原始文献"

with fitz.open(SOURCES / "Claude_Anthropic_2026.pdf") as document:
    document[0].get_pixmap(
        matrix=fitz.Matrix(1.65, 1.65),
        clip=fitz.Rect(70, 103, 542, 193),
    ).save(IMAGES / "16_claude_paper_heading.png")

with Image.open(IMAGES / "16_lamzouri_explaining.jpg") as photo:
    photo.thumbnail((480, 640))
    photo.save(IMAGES / "16_lamzouri_explaining_small.jpg", quality=94)

mp.mp.dps = 40
r = mp.mpf("0.5") + mp.cot(1 / mp.sqrt(2)) / mp.sqrt(2)
theta = mp.mpf("0.75")
short_interval = 2 - theta / 2 - mp.cot(theta / mp.sqrt(2)) / mp.sqrt(2)
assert mp.mpf("0.6725") < 2 - r < mp.mpf("0.67251")
assert short_interval > mp.mpf("0.419")
spread, concentrated = [1, 1, 1, 1], [4, 0, 0, 0]
assert sum(spread) == sum(concentrated) == 4
assert sum(x*x for x in spread) == 4
assert sum(x*x for x in concentrated) == 16
report = {
    "simple_and_on_line": str(2-r),
    "distinct": str((3-r)/2),
    "short_interval_theta_three_quarters": str(short_interval),
    "checks": "Arithmetic only; no verification of analytic estimates or Lean build.",
}
Path(__file__).with_name("16_arithmetic_checks.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(report, ensure_ascii=True, indent=2))
