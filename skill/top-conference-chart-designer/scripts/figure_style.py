"""Reusable Matplotlib style helpers for publication figures.

Import this module from a user-specific plotting script instead of treating it
as a complete chart generator. The data mapping and statistical choices remain
in that plotting script.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt


COLORBLIND_PALETTE = (
    "#0072B2",  # blue
    "#E69F00",  # orange
    "#009E73",  # green
    "#D55E00",  # vermilion
    "#CC79A7",  # purple
    "#56B4E9",  # sky blue
    "#F0E442",  # yellow
    "#4D4D4D",  # neutral
)


def apply_paper_style(font_size: float = 8.5) -> None:
    """Set restrained defaults; call before creating axes."""
    plt.rcParams.update(
        {
            "figure.facecolor": "white",
            "savefig.facecolor": "white",
            "font.size": font_size,
            "axes.labelsize": font_size,
            "axes.titlesize": font_size,
            "xtick.labelsize": max(font_size - 1, 6),
            "ytick.labelsize": max(font_size - 1, 6),
            "legend.fontsize": max(font_size - 1, 6),
            "axes.linewidth": 0.7,
            "lines.linewidth": 1.5,
            "lines.markersize": 4.5,
            "axes.grid": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )


def style_axes(ax, grid_axis: str | None = "y") -> None:
    """Remove nonessential spines and add a light optional guide grid."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="both", which="both", length=3, width=0.7)
    if grid_axis:
        ax.grid(axis=grid_axis, color="#D9D9D9", linewidth=0.55, alpha=0.65)
        ax.set_axisbelow(True)


def palette(n: int) -> list[str]:
    """Return a deterministic palette, cycling only when necessary."""
    if n <= 0:
        return []
    return [COLORBLIND_PALETTE[i % len(COLORBLIND_PALETTE)] for i in range(n)]


def save_figure(fig, output_stem: str | Path, dpi: int = 400) -> list[Path]:
    """Save PNG, PDF, and SVG siblings and return their paths."""
    stem = Path(output_stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    outputs = [stem.with_suffix(".png"), stem.with_suffix(".pdf"), stem.with_suffix(".svg")]
    fig.savefig(outputs[0], dpi=dpi, bbox_inches="tight", facecolor="white")
    fig.savefig(outputs[1], bbox_inches="tight", facecolor="white")
    fig.savefig(outputs[2], bbox_inches="tight", facecolor="white")
    return outputs
