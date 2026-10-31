# Interdisciplinary Index of industries

Rao–Stirling diversity of the disciplinary mix of professional staff in 11 U.S. industries. The mix is built from BLS OEWS occupational employment data (May 2022/2023).

The full description of data collection, the occupation-to-discipline mapping, the index formula and the limitations is in **[methods.md](methods.md)**.

## Layout

```
data/oews_industry_occupations.csv   raw BLS OEWS rows: industry, NAICS, release, source URL, SOC code, employment
src/disciplines.py                   discipline list, 2-D layout, distance matrix, diversity measures
src/compute_index.py                 occupation -> discipline mapping; computes shares and index
src/plot_figure.py                   8 x 4 in figure (German labels), ggplot2-style themes
results/                             generated: index.csv, discipline_shares.csv, bls_results.json
figures/                             generated: interdisz_bls_8x4_{minimal,classic,bw}.{png,pdf,svg}
```

## Reproduce

```bash
pip install -r requirements.txt
python src/compute_index.py      # writes results/
python src/plot_figure.py        # writes figures/ (all three themes; or pass minimal|classic|bw)
```

The figure uses the Liberation Sans font if it is installed; otherwise matplotlib falls back to its default font.

## Variants

`compute_index.py` computes three variants. The figure uses `all`.

| Variant | Included occupations |
|---|---|
| `all` | All professional occupations (SOC groups 11, 13, 15, 17, 19, 23, 27, 29) |
| `core` | As `all`, minus generic management and business roles |
| `notech` | As `all`, minus technicians (17-3, 19-4, 29-2) |
