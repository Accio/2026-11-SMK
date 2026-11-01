"""Netzwerk B, 4 x 6 in, min. 12 pt. Kanten nach Faktencheck.
Linienstärke = Evidenz; durchgezogen = setzt am Thema an, gestrichelt = stärkt Umgang mit Sorge.
"""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams.update({"font.size": 12, "font.family": "Liberation Sans",
                     "text.color": "#1A1A1A", "pdf.fonttype": 42,
                     "svg.fonttype": "none"})
TEXT, GREY = "#1A1A1A", "#4D4D4D"
CL = [  # (key, Label, Farbe, Mittelwert %)
    ("Krieg", "Krieg &\nSicherheit", "#F8766D", 27.4),
    ("Umwelt", "Umwelt &\nGesundheit", "#F564E3", 20.6),
    ("Politik", "Politik &\nDemokratie", "#B79F00", 25.9),
    ("Gerecht", "Gerechtigkeit\n& Toleranz", "#00BA38", 25.9),
    ("Digital", "Digitale Welt", "#00BFC4", 25.5),
    ("Wirtschaft", "Wirtschaft\n& Zukunft", "#619CFF", 24.4),
]
COL = {k: c for k, _, c, _ in CL}
EBENE = {"Politik": "#333333", "Schule": "#999999", "Individuum": "white"}
LW = {3: 4.0, 2: 2.7, 1: 1.6, 0: 0.9}

# (Label, Ebene, [(Cluster, Art u/s, Evidenz 0-3)]); 0 = im Faktencheck nicht belegt
A = [
    ("Dosierter\nNews-Konsum", "Individuum",
     [("Krieg", "s", 1), ("Umwelt", "s", 1), ("Politik", "s", 0)]),
    ("Kollektives\nEngagement", "Individuum",
     [("Umwelt", "s", 1), ("Gerecht", "u", 0), ("Krieg", "u", 0)]),
    ("Politische Bildung,\nMitsprache", "Schule",
     [("Politik", "u", 1), ("Wirtschaft", "u", 0), ("Umwelt", "u", 0)]),
    ("Antidiskriminierung,\nBegegnung", "Politik",
     [("Gerecht", "u", 2), ("Politik", "u", 0), ("Krieg", "u", 0)]),
    ("Medien- und\nKI-Kompetenz", "Schule",
     [("Digital", "u", 3), ("Politik", "u", 0), ("Gerecht", "u", 0)]),
    ("Wohnraum,\nLehrstellen,\nVorsorge", "Politik",
     [("Wirtschaft", "u", 1)]),
]

fig = plt.figure(figsize=(4, 6), facecolor="white")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 4); ax.set_ylim(0, 6); ax.axis("off")   # Koordinaten in Zoll

xa, xc = 1.9, 2.62
rows = [5.3 - i * 0.7 for i in range(6)]
ya = {a[0]: rows[i] for i, a in enumerate(A)}
yc = {k: rows[i] for i, (k, *_r) in enumerate(CL)}

ax.text(xa, 5.8, "Ansätze", ha="right", va="center", fontsize=12,
        fontweight="bold", color=GREY)
ax.text(xc, 5.8, "Themen", ha="left", va="center", fontsize=12,
        fontweight="bold", color=GREY)

for name, ebene, links in A:
    for c, art, ev in links:
        ax.plot([xa, xc], [ya[name], yc[c]], color=COL[c], lw=LW[ev],
                alpha=0.9 if ev else 0.45, ls="-" if art == "u" else (0, (2, 1.2)),
                zorder=2 if ev else 1, solid_capstyle="butt", dash_capstyle="butt")
for name, ebene, _ in A:
    ax.scatter(xa, ya[name], s=80, marker="s", color=EBENE[ebene],
               edgecolor="#333333", linewidth=1, zorder=3)
    ax.text(xa - 0.12, ya[name], name, ha="right", va="center", fontsize=12,
            color=TEXT, linespacing=1.05)
for k, lab, col, m in CL:
    ax.scatter(xc, yc[k], s=m * 10, color=col, edgecolor="white",
               linewidth=1.2, zorder=3)
    ax.text(xc + 0.17, yc[k], lab, ha="left", va="center", fontsize=12,
            color=TEXT, linespacing=1.05)

# Legende
def seg(x, y, **kw):
    ax.add_line(Line2D([x, x + 0.3], [y, y], color="#555555",
                       solid_capstyle="butt", **kw))

y = 1.27
for e, lab, x in [("Politik", "Politik", 0.12), ("Schule", "Schule", 1.12),
                  ("Individuum", "Individuum", 2.08)]:
    ax.scatter(x, y, s=70, marker="s", color=EBENE[e], edgecolor="#333333", zorder=3)
    ax.text(x + 0.12, y, lab, ha="left", va="center", fontsize=12, color=GREY)
seg(0.05, 1.0, lw=2.2)
ax.text(0.42, 1.0, "setzt am Thema an", ha="left", va="center", fontsize=12, color=GREY)
seg(0.05, 0.75, lw=2.2, ls=(0, (2, 1.2)))
ax.text(0.42, 0.75, "stärkt Umgang mit Sorge", ha="left", va="center",
        fontsize=12, color=GREY)
ax.text(0.05, 0.47, "Evidenz:", ha="left", va="center", fontsize=12, color=GREY)
for (lab, ev), (x, yy) in zip([("stark", 3), ("mittel", 2), ("schwach", 1), ("ungeprüft", 0)],
                              [(0.8, 0.47), (2.05, 0.47), (0.8, 0.2), (2.05, 0.2)]):
    seg(x, yy, lw=LW[ev], alpha=1 if ev else 0.5)
    ax.text(x + 0.37, yy, lab, ha="left", va="center", fontsize=12, color=GREY)

for ext in ("png", "pdf", "svg"):
    fig.savefig(f"netzwerk_loesungen_4x6.{ext}", dpi=300)
