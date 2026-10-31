"""Disciplines, their 2-D layout (stylised global map of science) and diversity measures."""
import numpy as np

DISC = ["bio", "chem", "med", "phys", "math", "cs", "eng", "soc", "econ", "law", "design"]

# Hand-set positions approximating the circular global map of science
# (Rafols, Porter & Leydesdorff 2010). Not estimated from citation data.
POS = {
    "math": (0.00, 1.00), "phys": (0.50, 0.90), "cs": (-0.50, 0.78), "eng": (0.88, 0.48),
    "chem": (1.00, -0.05), "bio": (0.72, -0.62), "med": (0.20, -0.98), "soc": (-0.55, -0.80),
    "law": (-0.92, -0.45), "econ": (-1.00, 0.02), "design": (-0.88, 0.48),
}


def dist_matrix(pos=POS):
    """Euclidean distances between discipline positions, scaled to [0, 1]."""
    X = np.array([pos[d] for d in DISC])
    D = np.linalg.norm(X[:, None] - X[None], axis=-1)
    return D / D.max()


def rao_stirling(p, D):
    """Rao-Stirling diversity: sum_{i!=j} p_i p_j d_ij (diagonal of D is 0)."""
    return float(p @ D @ p)


def gini(x):
    x = np.sort(x); n = len(x)
    return float((2 * np.arange(1, n + 1) - n - 1) @ x / (n * x.sum()))


def div(p, D, thr=0.02):
    """Leydesdorff, Wagner & Bornmann (2019) DIV = relative variety x Gini evenness x mean disparity."""
    m = p >= thr; q = p[m]; n = int(m.sum())
    if n < 2:
        return 0.0
    sub = D[np.ix_(m, m)]
    return float((n / len(p)) * (1 - gini(q)) * sub[np.triu_indices(n, 1)].mean())


def shannon(p):
    """Shannon entropy normalised to [0, 1]."""
    q = p[p > 0]
    return float(-(q * np.log(q)).sum() / np.log(len(p)))
