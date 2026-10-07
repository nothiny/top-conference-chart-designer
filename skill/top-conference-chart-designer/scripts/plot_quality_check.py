"""Lightweight checks for publication figure exports.

Usage:
    python plot_quality_check.py figure.png [figure.svg ...]

The script checks file existence, PNG dimensions/DPI, and basic vector-file
presence. It does not judge the scientific correctness of the plotted values.
"""
from __future__ import annotations

import sys
from pathlib import Path


def check_png(path: Path) -> list[str]:
    try:
        from PIL import Image
    except ImportError:
        return ["Pillow is unavailable; install it to inspect PNG metadata"]
    with Image.open(path) as image:
        width, height = image.size
        dpi = image.info.get("dpi", (0, 0))
        messages = []
        if width < 900 or height < 500:
            messages.append(f"PNG is small ({width}x{height}); verify final-size readability")
        if not dpi or min(dpi) < 250:
            messages.append(f"PNG DPI is {dpi}; target at least 300 DPI for paper export")
        return messages


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: plot_quality_check.py FIGURE [FIGURE ...]")
        return 2
    warnings = 0
    for name in argv:
        path = Path(name)
        if not path.exists():
            print(f"ERROR missing: {path}")
            warnings += 1
            continue
        suffix = path.suffix.lower()
        messages = check_png(path) if suffix == ".png" else []
        if suffix in {".svg", ".pdf"} and path.stat().st_size < 1024:
            messages.append("vector file is unusually small; verify it contains the figure")
        if messages:
            warnings += len(messages)
            for message in messages:
                print(f"WARN {path}: {message}")
        else:
            print(f"OK {path}")
    return 1 if warnings else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
