"""Prepare sourced display assets; arithmetic examples are not PDE simulations."""
from pathlib import Path
from fractions import Fraction
import fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
IMAGE_DIR = ROOT / "04_第四篇_AI新纪元" / "img"
SOURCE_DIR = ROOT / "资料" / "17_NS爆破与722篇论文" / "原始文献"

with fitz.open(SOURCE_DIR / "OpenAI_NS_2026.pdf") as document:
    document[3].get_pixmap(
        matrix=fitz.Matrix(1.8, 1.8), clip=fitz.Rect(88, 82, 520, 275)
    ).save(IMAGE_DIR / "17_ns_vortex_paper.png")

with Image.open(IMAGE_DIR / "17_cordoba_zoroa.jpg") as photo:
    photo.thumbnail((900, 600))
    photo.save(IMAGE_DIR / "17_cordoba_zoroa_small.jpg", quality=93)

pairs = [(1, 1), (-1, -1)]
assert sum(x for x, _ in pairs) == 0
assert sum(y for _, y in pairs) == 0
assert sum(x*y for x, y in pairs) / len(pairs) == 1
# For all 0 < h < 1/100, 1/2 - 3h > 47/100 > 0.
assert Fraction(1, 2) - 3*Fraction(1, 100) == Fraction(47, 100)
print("Assets prepared; toy average and energy exponent arithmetic checked. No PDE or Lean verification.")
