"""BLS-only (alle Fachberufe) Interdisciplinary Index figure, German labels, 8 x 4 in, ggplot2-like themes.
Usage: python src/plot_figure.py [minimal|classic|bw]   (default: all three)
Requires results/bls_results.json (run src/compute_index.py first)."""
import sys, json
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from disciplines import DISC

ROOT = Path(__file__).resolve().parent.parent

R = json.load(open(ROOT / "results" / "bls_results.json"))
NAME = dict(rnd_svc="F&E-Dienstleistungen", pharma="Pharma", meddev="Medizintechnik",
            auto="Kraftfahrzeugbau", aerospace="Luft- und Raumfahrt", ae_services="Architektur/Ingenieurbüros",
            semis="Halbleiter", food="Lebensmittelherstellung", consulting="Unternehmensberatung",
            software="Softwareverlage", legal="Rechtsdienstleistungen")
DNAME = dict(bio="Biologie", chem="Chemie", med="Medizin", phys="Physik", math="Mathe/Statistik", cs="Informatik",
             eng="Ingenieurwesen", soc="Sozialwiss.", econ="Wirtschaft", law="Recht/Regulierung", design="Design/Medien")
SET3 = ["#8DD3C7", "#FFFFB3", "#BEBADA", "#FB8072", "#80B1D3", "#FDB462",
        "#B3DE69", "#FCCDE5", "#D9D9D9", "#BC80BD", "#CCEBC5"]   # RColorBrewer Set3, first 11
GRID, BORDER, TEXT, TICK = "#EBEBEB", "#333333", "#1A1A1A", "#4D4D4D"
HIGHLIGHT = "#4D4D4D"


def style_axes(ax, theme):
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(colors=TICK, labelcolor=TICK)
    ax.xaxis.label.set_color(TEXT)
    if theme == "minimal":
        ax.xaxis.grid(True, color=GRID, lw=0.8); ax.tick_params(length=0)
    elif theme == "classic":
        for side in ("left", "bottom"):
            ax.spines[side].set_visible(True); ax.spines[side].set_color("black"); ax.spines[side].set_linewidth(0.8)
        ax.tick_params(axis="x", length=3, width=0.8, color="black"); ax.tick_params(axis="y", length=0)
    elif theme == "bw":
        for s in ax.spines.values():
            s.set_visible(True); s.set_color(BORDER); s.set_linewidth(0.8)
        ax.xaxis.grid(True, color=GRID, lw=0.8)
        ax.tick_params(axis="x", length=3, width=0.8, color=BORDER); ax.tick_params(axis="y", length=0)
    ax.set_axisbelow(True)


def make(theme):
    plt.rcParams.update({"font.size": 12, "font.family": "Liberation Sans", "text.color": TEXT,
                         "pdf.fonttype": 42, "svg.fonttype": "none"})
    fig = plt.figure(figsize=(8, 4), facecolor="white")
    keys = sorted(R, key=lambda k: R[k]["all"]["rs"])          # bottom = lowest
    y = np.arange(len(keys))
    rs = [R[k]["all"]["rs"] for k in keys]

    # Panel A: Rao-Stirling diversity
    ax = fig.add_axes([0.265, 0.13, 0.165, 0.80])
    cols = [HIGHLIGHT if k == "pharma" else "#BDBDBD" for k in keys]
    ax.barh(y, rs, color=cols, height=0.68)
    ax.set_yticks(y, [NAME[k] for k in keys]); ax.set_ylim(-0.6, len(keys) - 0.4)
    ax.set_xlim(0, 0.62); ax.set_xticks([0, 0.3, 0.6], ["0", "0.3", "0.6"])
    ax.set_xlabel("Interdisciplinary Index", labelpad=3)
    style_axes(ax, theme)
    for tl, k in zip(ax.get_yticklabels(), keys):
        if k == "pharma": tl.set_fontweight("bold"); tl.set_color(TEXT)
    fig.text(0.008, 0.985, "A", fontweight="bold", va="top", fontsize=18)

    # Panel B: discipline mix (stacked, %)
    bx = fig.add_axes([0.475, 0.13, 0.29, 0.80])
    left = np.zeros(len(keys))
    for j, (d, c) in enumerate(zip(DISC, SET3)):
        v = np.array([R[k]["all"]["p"][j] for k in keys]) * 100
        bx.barh(y, v, left=left, color=c, height=0.68, edgecolor="white", lw=0.4, label=DNAME[d])
        for yi, (l, vv) in enumerate(zip(left, v)):
            if vv >= 15: bx.text(l + vv / 2, yi, f"{vv:.0f}", ha="center", va="center", fontsize=12, color=TEXT)
        left += v
    bx.set_yticks(y, []); bx.set_ylim(-0.6, len(keys) - 0.4)
    bx.set_xlim(0, 100); bx.set_xticks([0, 25, 50, 75, 100])
    bx.set_xlabel("Anteil der Fachkräfte (%)", labelpad=3)
    style_axes(bx, theme)
    fig.text(0.455, 0.985, "B", fontweight="bold", va="top", fontsize=18)
    fig.legend(*bx.get_legend_handles_labels(), loc="center left", bbox_to_anchor=(0.768, 0.53), frameon=False,
               handlelength=1, handleheight=1, handletextpad=0.4, labelspacing=0.3, fontsize=12)

    for ext in ("png", "pdf", "svg"):
        fig.savefig(ROOT / "figures" / f"interdisz_bls_8x4_{theme}.{ext}", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    for t in sys.argv[1:] or ["minimal", "classic", "bw"]:
        make(t)
