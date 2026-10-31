"""Map BLS OEWS occupations to disciplines and compute the Interdisciplinary Index per industry.

Usage:  python src/compute_index.py
Input:  data/oews_industry_occupations.csv
Output: results/discipline_shares.csv, results/index.csv, results/bls_results.json
"""
import csv, json
from collections import defaultdict
from pathlib import Path
import numpy as np
from disciplines import DISC, dist_matrix, rao_stirling, div, shannon

ROOT = Path(__file__).resolve().parent.parent
PROFESSIONAL_GROUPS = ("11", "13", "15", "17", "19", "23", "27", "29")

# ---- explicit occupation -> discipline rules (fractions sum to 1) ----
EXACT = {
    "11-9041": dict(eng=1), "11-3021": dict(cs=1), "11-9111": dict(med=1), "11-3051": dict(eng=.5, econ=.5),
    "11-9121": "SCI",                                   # natural sciences managers -> industry's own scientist mix
    "13-1041": dict(law=1),                             # compliance officers (incl. regulatory affairs)
    "17-1011": dict(design=1), "17-1012": dict(design=1),
    "17-2031": dict(eng=.6, bio=.2, med=.2), "17-2041": dict(eng=.5, chem=.5), "17-2131": dict(eng=.5, chem=.25, phys=.25),
    "19-1012": dict(bio=.5, chem=.5), "19-1021": dict(bio=.5, chem=.5), "19-1041": dict(med=.5, math=.5),
    "19-1042": dict(med=.5, bio=.5),
    "19-2011": dict(phys=1), "19-2012": dict(phys=1), "19-2021": dict(phys=1), "19-2031": dict(chem=1),
    "19-2032": dict(chem=.5, phys=.5), "19-2041": dict(bio=.5, chem=.25, phys=.25), "19-2042": dict(phys=1),
    "19-2043": dict(phys=1), "19-2099": dict(phys=.5, chem=.5), "19-3011": dict(econ=1), "19-3051": dict(soc=.5, design=.5),
    "19-4012": dict(bio=1), "19-4013": dict(bio=.5, chem=.5), "19-4021": dict(bio=1), "19-4031": dict(chem=1),
    "19-4042": dict(bio=.5, chem=.25, phys=.25), "19-4043": dict(phys=1), "19-4044": dict(phys=1), "19-4051": dict(phys=1),
    "19-4061": dict(soc=1), "19-4071": dict(bio=1), "19-4092": dict(chem=1), "19-4099": "SCI",
    "19-5011": dict(eng=.5, med=.5), "19-5012": dict(eng=.5, med=.5),
    "29-1051": dict(med=.5, chem=.5), "29-1131": dict(bio=.5, med=.5), "29-2056": dict(bio=.5, med=.5),
    "29-2091": dict(med=.5, eng=.5),
}


def prefix_rule(code):
    g = code[:2]
    if g in ("11", "13"): return dict(econ=1)
    if g == "15": return dict(math=1) if code.startswith("15-2") else dict(cs=1)
    if g == "17": return dict(eng=1)
    if code.startswith("19-1"): return dict(bio=1)
    if code.startswith("19-2"): return dict(phys=.5, chem=.5)
    if code.startswith("19-3"): return dict(soc=1)
    if g == "23": return dict(law=1)
    if g == "27": return dict(design=1)
    if g == "29": return dict(med=1)
    return None


GENERIC_BUSINESS = lambda c: c[:2] in ("11", "13") and c not in ("11-9041", "11-3021", "11-9111", "11-9121", "13-1041")
TECHNICIAN = lambda c: c.startswith(("17-3", "19-4", "29-2"))


def shares(occ, variant="all"):
    """variant: 'all' = all professional occupations (used in the figure);
    'core' = generic management/business removed; 'notech' = technicians removed."""
    v = {d: 0.0 for d in DISC}; pending = 0.0
    for c, n in occ.items():
        if c[:2] not in PROFESSIONAL_GROUPS: continue
        if variant == "core" and GENERIC_BUSINESS(c): continue
        if variant == "notech" and TECHNICIAN(c): continue
        r = EXACT.get(c) or prefix_rule(c)
        if r == "SCI": pending += n; continue
        for d, f in r.items(): v[d] += f * n
    sci = np.array([v[d] for d in ("bio", "chem", "phys")])
    if pending and sci.sum() > 0:
        for d, s in zip(("bio", "chem", "phys"), sci / sci.sum()): v[d] += pending * s
    p = np.array([v[d] for d in DISC])
    return p / p.sum(), float(p.sum())


def load():
    data, meta = defaultdict(dict), {}
    with open(ROOT / "data" / "oews_industry_occupations.csv") as f:
        for r in csv.DictReader(f):
            data[r["industry_key"]][r["soc_code"]] = int(r["employment"])
            meta[r["industry_key"]] = dict(naics=r["naics"], release=r["oews_release"], url=r["source_url"])
    return data, meta


if __name__ == "__main__":
    data, meta = load(); D = dist_matrix(); out = {}
    for k, occ in data.items():
        out[k] = dict(meta=meta[k])
        for var in ("all", "core", "notech"):
            p, n = shares(occ, var)
            out[k][var] = dict(p=p.tolist(), n=n, rs=rao_stirling(p, D), div=div(p, D), sh=shannon(p))
    (ROOT / "results").mkdir(exist_ok=True)
    json.dump(out, open(ROOT / "results" / "bls_results.json", "w"), indent=1)
    keys = sorted(out, key=lambda k: -out[k]["all"]["rs"])
    with open(ROOT / "results" / "index.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["industry_key", "naics", "oews_release", "n_professional",
                    "index_all", "index_core", "index_notech", "div_all", "shannon_all"])
        for k in keys:
            r = out[k]
            w.writerow([k, r["meta"]["naics"], r["meta"]["release"], round(r["all"]["n"]),
                        *(round(r[v]["rs"], 4) for v in ("all", "core", "notech")),
                        round(r["all"]["div"], 4), round(r["all"]["sh"], 4)])
    with open(ROOT / "results" / "discipline_shares.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["industry_key", "variant", *DISC])
        for k in keys:
            for v in ("all", "core", "notech"):
                w.writerow([k, v, *(round(x, 4) for x in out[k][v]["p"])])
    for k in keys:
        print(f"{k:12s} n={out[k]['all']['n']:>9.0f}  index={out[k]['all']['rs']:.3f}")
