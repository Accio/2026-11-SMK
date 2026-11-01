"""Pro Juventute Jugendstudie 2026, Abbildung 4 (gesamt), clustered into 6 panels.
Usage: python worries_figure.py [minimal|classic|bw]   (default: all three)
"""
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# % of all respondents worried "ziemlich" or "sehr" (Abbildung 4, gesamt, N = 960)
clusters = {
    "Krieg & Sicherheit": [
        ("Kriege", 39.7),
        ("Kriminalität, Gewalt", 29.6),
        ("Flüchtlingskrise", 20.6),
        ("Unsicherheit CH", 19.6),
    ],
    "Politik & Demokratie": [
        ("Weltpolitik, Krisen", 35.4),
        ("Antidemokratisch", 29.9),
        ("Polarisierung CH", 23.3),
        ("Politik Schweiz", 15.1),
    ],
    "Gerechtigkeit & Toleranz": [
        ("Ungerechtigkeit", 30.7),
        ("Sexismus", 29.2),
        ("Rassismus", 23.7),
        ("Fehlende Toleranz", 20.0),
    ],
    "Digitale Welt": [
        ("Fake News, KI", 30.0),
        ("Digitale Macht", 20.9),
    ],
    "Wirtschaft & Zukunft": [
        ("Zukunft allgemein", 35.8),
        ("Wohnkosten", 22.6),
        ("Wirtschaft, Inflation", 20.3),
        ("Renten", 18.9),
    ],
    "Umwelt & Gesundheit": [
        ("Klimawandel", 31.6),
        ("Artensterben", 25.5),
        ("Pandemien", 4.7),
    ],
}
# order panels by cluster mean (descending); bars within a panel by value
clusters = dict(sorted(clusters.items(),
                       key=lambda kv: -sum(v for _, v in kv[1]) / len(kv[1])))
COLORS = ["#F8766D", "#B79F00", "#00BA38", "#00BFC4", "#619CFF", "#F564E3"]

GRID, BORDER, TEXT, TICK_TEXT = "#EBEBEB", "#333333", "#1A1A1A", "#4D4D4D"
W, H = 4.0, 6.0                      # inches
PT = 1 / 72                          # inch per point
XMAX = 47.5


def make(theme):
    plt.rcParams.update({"font.size": 12, "font.family": "Liberation Sans",
                         "text.color": TEXT, "pdf.fonttype": 42,
                         "svg.fonttype": "none"})
    fig = plt.figure(figsize=(W, H), facecolor="white")

    left, right = 1.50 / W, 0.06 / W        # room for category labels
    top_pad, bottom_pad = 4 * PT / H, 40 * PT / H
    strip_h = 17 * PT / H
    gap = 4 * PT / H
    n_bars = sum(len(v) for v in clusters.values())
    avail = 1 - top_pad - bottom_pad - len(clusters) * (strip_h + gap) + gap
    row_h = avail / n_bars

    y = 1 - top_pad
    axes = []
    for i, (name, items) in enumerate(clusters.items()):
        # strip
        sax = fig.add_axes([left, y - strip_h, 1 - left - right, strip_h])
        sax.set_xticks([]); sax.set_yticks([])
        for s in sax.spines.values():
            s.set_visible(False)
        if theme == "bw":
            sax.add_patch(Rectangle((0, 0), 1, 1, transform=sax.transAxes,
                                    facecolor="#D9D9D9", edgecolor=BORDER, lw=0.8))
        elif theme == "classic":
            sax.add_patch(Rectangle((0, 0), 1, 1, transform=sax.transAxes,
                                    facecolor="white", edgecolor="black", lw=0.8))
        sax.text(0.02 if theme != "minimal" else 0.0, 0.5, name,
                 transform=sax.transAxes, va="center", ha="left",
                 fontsize=12, color=TEXT)
        y -= strip_h

        # panel
        h = row_h * len(items)
        ax = fig.add_axes([left, y - h, 1 - left - right, h])
        items = sorted(items, key=lambda t: t[1])
        labels = [l for l, _ in items]
        vals = [v for _, v in items]
        pos = range(len(items))
        ax.barh(pos, vals, height=0.72, color=COLORS[i], zorder=2)
        for p, v in zip(pos, vals):
            ax.text(v + 0.8, p, f"{v:.1f}", va="center", ha="left",
                    fontsize=12, color=TEXT, zorder=3)
        ax.set_yticks(list(pos), labels)
        ax.set_ylim(-0.6, len(items) - 0.4)
        ax.set_xlim(0, XMAX)
        ax.set_xticks([0, 10, 20, 30, 40])
        ax.tick_params(labelsize=12, colors=TICK_TEXT, labelcolor=TICK_TEXT,
                       length=0, pad=3)
        for s in ax.spines.values():
            s.set_visible(False)
        if theme in ("minimal", "bw"):
            ax.xaxis.grid(True, color=GRID, lw=0.8, zorder=0)
        if theme == "bw":
            for s in ax.spines.values():
                s.set_visible(True); s.set_color(BORDER); s.set_linewidth(0.8)
        if theme == "classic":
            ax.spines["left"].set_visible(True)
            ax.spines["left"].set_color("black")
            ax.spines["left"].set_linewidth(0.8)
        last = i == len(clusters) - 1
        if not last:
            ax.tick_params(axis="x", labelbottom=False)
        else:
            if theme == "classic":
                ax.spines["bottom"].set_visible(True)
                ax.spines["bottom"].set_color("black")
                ax.spines["bottom"].set_linewidth(0.8)
                ax.tick_params(axis="x", length=3, width=0.8, color="black")
            ax.set_xlabel("% ziemlich oder sehr besorgt", fontsize=12,
                          color=TEXT, labelpad=3)
        axes.append(ax)
        y -= h + gap

    for ext in ("png", "pdf", "svg"):
        fig.savefig(f"sorgen_{theme}.{ext}", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    for t in sys.argv[1:] or ["minimal", "classic", "bw"]:
        make(t)
