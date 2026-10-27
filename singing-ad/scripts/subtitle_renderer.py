#!/usr/bin/env python3
"""Render singing-ad subtitles as transparent PNG overlays.

Fallback for ffmpeg without libass. Each subtitle line becomes a PNG
with white bold text + black outline, composited via ffmpeg concat + overlay.

Usage:
    from subtitle_renderer import render_subtitle_pngs
    render_subtitle_pngs(timing_json, output_dir, width=1080, height=1920)
"""

import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_SIZE = 66
STROKE_WIDTH = 7
MAX_TEXT_WIDTH = 920
BOTTOM_OFFSET = 560
LINE_SPACING = 10


def _find_font():
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return p
    return None


def _wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_width and current:
            lines.append(current)
            current = word
        else:
            current = test
    if current:
        lines.append(current)
    return lines


def render_subtitle_png(text, output_path, width=1080, height=1920):
    font_path = _find_font()
    if font_path:
        font = ImageFont.truetype(font_path, FONT_SIZE)
    else:
        font = ImageFont.load_default()

    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    lines = _wrap_text(draw, text, font, MAX_TEXT_WIDTH)

    line_heights = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_heights.append(bbox[3] - bbox[1])

    total_h = sum(line_heights) + LINE_SPACING * (len(lines) - 1)
    y_start = height - BOTTOM_OFFSET - total_h

    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_w = bbox[2] - bbox[0]
        x = (width - text_w) // 2
        y = y_start + sum(line_heights[:i]) + LINE_SPACING * i

        draw.text(
            (x, y), line, font=font, fill="white",
            stroke_width=STROKE_WIDTH, stroke_fill="black",
            anchor="la",
        )

    img.save(output_path, "PNG")
    return output_path


def render_subtitle_pngs(timing_json_path, output_dir, width=1080, height=1920):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(timing_json_path) as f:
        timing = json.load(f)

    results = []
    for i, entry in enumerate(timing):
        text = entry.get("text", entry.get("line", ""))
        if not text.strip():
            continue
        out_path = output_dir / f"sub_{i:04d}.png"
        render_subtitle_png(text, str(out_path), width, height)
        results.append({
            "index": i,
            "text": text,
            "start": entry["start"],
            "end": entry["end"],
            "png": str(out_path),
        })

    return results


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 subtitle_renderer.py <timing.json> <output_dir>")
        sys.exit(1)
    results = render_subtitle_pngs(sys.argv[1], sys.argv[2])
    print(f"Rendered {len(results)} subtitle frames")
