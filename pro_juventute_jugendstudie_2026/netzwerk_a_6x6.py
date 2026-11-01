"""Netzwerk A nach Faktencheck, 6 x 6 in, min. 12 pt.
Knotengrösse = % ziemlich/sehr besorgt (Abb. 4). Linienstärke = Evidenz für den Zusammenhang.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D

plt.rcParams.update({"font.size": 12, "font.family": "Liberation Sans",
                     "text.color": "#1A1A1A", "pdf.fonttype": 42,
                     "svg.fonttype": "none"})
TEXT, GREY, EDGE = "#1A1A1A", "#4D4D4D", "#3A3A3A"

CL = {
    "Politik & Demokratie":     ("#B79F00", (0.1, 7.35, 4.95, 9.95)),
    "Digitale Welt":            ("#00BFC4", (5.05, 7.35, 9.9, 9.95)),
    "Krieg & Sicherheit":       ("#F8766D", (0.1, 3.95, 4.95, 6.55)),
    "Gerechtigkeit & Toleranz": ("#00BA38", (5.05, 3.95, 9.9, 6.55)),
    "Umwelt & Gesundheit":      ("#F564E3", (0.1, 0.55, 4.95, 3.15)),
    "Wirtschaft & Zukunft":     ("#619CFF", (5.05, 0.55, 9.9, 3.15)),
}
N = {
    "Politik Schweiz":       ("Politik & Demokratie", 15.1, 1.5, 9.0),
    "Polarisierung CH":      ("Politik & Demokratie", 23.3, 3.75, 9.0),
    "Weltpolitik, Krisen":   ("Politik & Demokratie", 35.4, 1.5, 7.95),
    "Antidemokratisch":      ("Politik & Demokratie", 29.9, 3.75, 7.95),
    "Fake News, KI":         ("Digitale Welt", 30.0, 6.3, 8.45),
    "Digitale Macht":        ("Digitale Welt", 20.9, 8.55, 8.45),
    "Unsicherheit CH":       ("Krieg & Sicherheit", 19.6, 1.5, 5.6),
    "Kriege":                ("Krieg & Sicherheit", 39.7, 3.75, 5.6),
    "Flüchtlingskrise":      ("Krieg & Sicherheit", 20.6, 1.5, 4.55),
    "Kriminalität, Gewalt":  ("Krieg & Sicherheit", 29.6, 3.75, 4.55),
    "Rassismus":             ("Gerechtigkeit & Toleranz", 23.7, 6.3, 5.6),
    "Fehlende Toleranz":     ("Gerechtigkeit & Toleranz", 20.0, 8.55, 5.6),
    "Sexismus":              ("Gerechtigkeit & Toleranz", 29.2, 6.3, 4.55),
    "Ungerechtigkeit":       ("Gerechtigkeit & Toleranz", 30.7, 8.55, 4.55),
    "Artensterben":          ("Umwelt & Gesundheit", 25.5, 1.5, 2.2),
    "Klimawandel":           ("Umwelt & Gesundheit", 31.6, 3.75, 2.2),
    "Pandemien":             ("Umwelt & Gesundheit", 4.7, 1.5, 1.15),
    "Wirtschaft, Inflation": ("Wirtschaft & Zukunft", 20.3, 6.3, 2.2),
    "Wohnkosten":            ("Wirtschaft & Zukunft", 22.6, 8.55, 2.2),
    "Zukunft allgemein":     ("Wirtschaft & Zukunft", 35.8, 6.3, 1.15),
    "Renten":                ("Wirtschaft & Zukunft", 18.9, 8.55, 1.15),
}

# (a, b, Evidenz) 3 = stark, 2 = mittel, 1 = schwach, 0 = ungeprüft. Quellen: siehe Antwort im Chat.
E = [
    ("Kriege", "Flüchtlingskrise", 3),           # UNHCR Global Trends 2025
    ("Kriege", "Wirtschaft, Inflation", 3),      # EZB: Energie/Nahrung > 2/3 der Inflation 2022
    ("Kriege", "Weltpolitik, Krisen", 2),        # ETH Sicherheit 2024
    ("Kriege", "Unsicherheit CH", 2),            # ETH Sicherheit 2024
    ("Weltpolitik, Krisen", "Unsicherheit CH", 2),
    ("Weltpolitik, Krisen", "Antidemokratisch", 2),   # V-Dem 2026
    ("Kriege", "Rassismus", 1),                  # NEU: Rassismusbericht 2024 (geopolit. Lage)
    ("Antidemokratisch", "Fake News, KI", 1),    # Lorenz-Spreen 2022; Altay
    ("Antidemokratisch", "Rassismus", 0),
    ("Antidemokratisch", "Fehlende Toleranz", 0),
    ("Polarisierung CH", "Digitale Macht", 2),   # Lorenz-Spreen 2022
    ("Polarisierung CH", "Fake News, KI", 1),    # Altay: eher umgekehrte Richtung
    ("Polarisierung CH", "Fehlende Toleranz", 1),  # Druckman & Levy
    ("Polarisierung CH", "Politik Schweiz", 1),  # Fraktionsdisziplin seit 2003 gestiegen
    ("Polarisierung CH", "Rassismus", 1),        # NEU: Rassismusbericht 2024
    ("Fake News, KI", "Digitale Macht", 0),
    ("Klimawandel", "Artensterben", 3),          # IPBES
    ("Klimawandel", "Ungerechtigkeit", 3),       # IPCC AR6 WG2 Kap. 8 (high confidence)
    ("Klimawandel", "Zukunft allgemein", 3),     # Hickman 2021, 10'000 Junge
    ("Klimawandel", "Flüchtlingskrise", 1),      # Hoffmann 2020: v.a. Binnenmigration
    ("Klimawandel", "Pandemien", 3),             # NEU: IPBES 2020
    ("Artensterben", "Pandemien", 3),            # IPBES 2020
    ("Ungerechtigkeit", "Wirtschaft, Inflation", 2),  # CEPR/VoxEU 2022
    ("Ungerechtigkeit", "Wohnkosten", 0),
    ("Wirtschaft, Inflation", "Wohnkosten", 2),  # Referenzzinssatz 2023
    ("Wirtschaft, Inflation", "Renten", 0),
    ("Renten", "Zukunft allgemein", 1),          # gemeinsamer Alterseffekt Jugendstudie
    ("Wohnkosten", "Zukunft allgemein", 1),
    ("Sexismus", "Kriminalität, Gewalt", 3),     # BFS PKS 2025
    ("Sexismus", "Rassismus", 1),                # Jugendstudie: Frauen, Migration
    ("Rassismus", "Fehlende Toleranz", 0),
    ("Kriminalität, Gewalt", "Unsicherheit CH", 2),  # Crime Survey 2025
]
LW = {3: 3.6, 2: 2.3, 1: 1.3, 0: 0.8}

fig = plt.figure(figsize=(6, 6), facecolor="white")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 10); ax.set_ylim(-1.3, 10.05); ax.axis("off")

for name, (col, (x0, y0, x1, y1)) in CL.items():
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                 boxstyle="round,pad=0,rounding_size=0.25",
                 fc=col, alpha=0.10, ec="none", zorder=0))
    ax.text(x0 + 0.15, y1 - 0.12, name, ha="left", va="top", fontsize=12,
            fontweight="bold", color=col, zorder=5,
            bbox=dict(fc="white", ec="none", alpha=0.85, pad=1))

for a, b, ev in sorted(E, key=lambda e: e[2]):
    xa, ya = N[a][2:]; xb, yb = N[b][2:]
    ax.plot([xa, xb], [ya, yb], color=EDGE if ev else "#9A9A9A",
            lw=LW[ev], alpha=0.75 if ev else 0.6, zorder=1 + ev * 0.1,
            solid_capstyle="round")

for k, (c, v, x, y) in N.items():
    ax.scatter(x, y, s=v * 13, color=CL[c][0], edgecolor="white",
               linewidth=1.2, zorder=3)
    ax.text(x, y - 0.33, k, ha="center", va="top", fontsize=12, color=TEXT,
            zorder=4, bbox=dict(fc="white", ec="none", alpha=0.8, pad=0.5))

# Legende
ly1, ly2 = -0.25, -0.85
ax.text(0.15, ly1, "Besorgt:", ha="left", va="center", fontsize=12, color=GREY)
for x, v in [(1.85, 10), (3.3, 20), (4.85, 40)]:
    ax.scatter(x, ly1, s=v * 13, color="#BBBBBB", edgecolor="white", zorder=3)
    ax.text(x + (0.45 if v == 40 else 0.32), ly1, f"{v} %", ha="left",
            va="center", fontsize=12, color=GREY)
ax.text(0.15, ly2, "Evidenz:", ha="left", va="center", fontsize=12, color=GREY)
for (lab, ev), x in zip([("stark", 3), ("mittel", 2), ("schwach", 1), ("ungeprüft", 0)],
                        [1.65, 3.6, 5.6, 7.75]):
    ax.add_line(Line2D([x, x + 0.6], [ly2, ly2], color=EDGE if ev else "#9A9A9A",
                       lw=LW[ev], alpha=0.75 if ev else 0.6, solid_capstyle="butt"))
    ax.text(x + 0.72, ly2, lab, ha="left", va="center", fontsize=12, color=GREY)

for ext in ("png", "pdf", "svg"):
    fig.savefig(f"netzwerk_themen_6x6.{ext}", dpi=300)
