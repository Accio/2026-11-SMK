# Interdisciplinary Index of industries — data and methods

Companion to `figures/interdisz_bls_8x4_{minimal,classic,bw}.{png,pdf}`. Raw data: `data/oews_industry_occupations.csv`. Code: `src/compute_index.py` (mapping and index), `src/disciplines.py` (distance layout and measures), `src/plot_figure.py` (figure).

## 1. Data collection

**Source.** U.S. Bureau of Labor Statistics, *Occupational Employment and Wage Statistics* (OEWS), national industry-specific estimates. OEWS is a semi-annual establishment survey. Each industry page reports employment for every detailed occupation (6-digit SOC 2018 code) within that industry (NAICS code).

**Industries and reference periods.** The pages below were retrieved on 31 Oct 2026. May 2023 was used where it was reachable. Semiconductors and consulting use May 2022 because the 2023 pages were not accessible from this environment.

| Figure label (DE) | Industry | NAICS | OEWS release | Professional employees used |
|---|---|---|---|---|
| F&E-Dienstleistungen | Research & development in the physical, engineering and life sciences | 541710 | May 2023 | 735,660 |
| Pharma | Pharmaceutical and medicine manufacturing | 3254 | May 2023 | 158,240 |
| Medizintechnik | Medical equipment and supplies manufacturing | 3391 | May 2023 | 92,580 |
| Kraftfahrzeugbau | Motor vehicle manufacturing | 3361 | May 2023 | 46,410 |
| Luft- und Raumfahrt | Aerospace product and parts manufacturing | 3364 | May 2023 | 254,830 |
| Architektur/Ingenieurbüros | Architectural, engineering and related services | 5413 | May 2023 | 1,310,390 |
| Halbleiter | Semiconductor and other electronic component manufacturing | 3344 | May 2022 | 164,540 |
| Lebensmittelherstellung | Food manufacturing | 311 | May 2023 | 153,810 |
| Unternehmensberatung | Management, scientific and technical consulting services | 5416 | May 2022 | 1,234,220 |
| Softwareverlage | Software publishers | 5132 | May 2023 | 525,960 |
| Rechtsdienstleistungen | Legal services | 5411 | May 2023 | 859,660 |

URLs follow the pattern `https://www.bls.gov/oes/<year>/may/naics<level>_<code>.htm`. Every row of `data/oews_industry_occupations.csv` carries its source URL.

**Inclusion rule ("alle Fachberufe").** Only detailed occupations in the SOC major groups for professional and knowledge work were kept:

- 11 Management
- 13 Business and financial operations
- 15 Computer and mathematical
- 17 Architecture and engineering
- 19 Life, physical and social science
- 23 Legal
- 27 Arts, design, entertainment, sports and media
- 29 Healthcare practitioners and technical

Production, sales, office/administrative, maintenance, transport and other operational groups were excluded. Estimates that BLS suppresses (shown as "(8)") were set to 0.

## 2. Mapping occupations to disciplines

Each occupation was assigned to one or more of 11 disciplines. Occupations that span disciplines were split by fixed fractions. The rules are applied in order: explicit code rules first, then prefix defaults.

**Explicit rules (selection; full list in `src/compute_index.py`, dict `EXACT`)**

| SOC | Occupation | Discipline(s) |
|---|---|---|
| 11-9041 | Architectural & engineering managers | Engineering |
| 11-3021 | Computer & information systems managers | Computer science |
| 11-9111 | Medical & health services managers | Medicine |
| 11-3051 | Industrial production managers | ½ Engineering, ½ Business |
| 11-9121, 19-4099 | Natural sciences managers; science technicians n.e.c. | Distributed over Biology/Chemistry/Physics in proportion to the industry's own scientist mix |
| 13-1041 | Compliance officers (includes regulatory affairs) | Law/Regulation |
| 17-1011, 17-1012 | Architects, landscape architects | Design |
| 17-2031 | Bioengineers & biomedical engineers | 0.6 Engineering, 0.2 Biology, 0.2 Medicine |
| 17-2041 | Chemical engineers | ½ Engineering, ½ Chemistry |
| 17-2131 | Materials engineers | ½ Engineering, ¼ Chemistry, ¼ Physics |
| 19-1021 | Biochemists & biophysicists | ½ Biology, ½ Chemistry |
| 19-1042 | Medical scientists | ½ Medicine, ½ Biology |
| 19-1041 | Epidemiologists | ½ Medicine, ½ Math/Statistics |
| 19-2031, 19-4031 | Chemists, chemical technicians | Chemistry |
| 19-2012 etc. | Physicists, astronomers, atmospheric and geoscientists | Physics |
| 19-2041 | Environmental scientists | ½ Biology, ¼ Chemistry, ¼ Physics |
| 19-3011 | Economists | Business/Economics |
| 19-5011, 19-5012 | Occupational health & safety | ½ Engineering, ½ Medicine |
| 29-1051 | Pharmacists | ½ Medicine, ½ Chemistry |
| 29-1131 | Veterinarians | ½ Biology, ½ Medicine |

**Prefix defaults (all other codes)**

| SOC prefix | Discipline |
|---|---|
| 11-, 13- | Business/Economics |
| 15-1 | Computer science |
| 15-2 | Math/Statistics |
| 17- | Engineering |
| 19-1 | Biology |
| 19-2 | ½ Physics, ½ Chemistry |
| 19-3 | Social/behavioural sciences |
| 23- | Law/Regulation |
| 27- | Design/Media |
| 29- | Medicine |

For each industry, the mapped employment is summed by discipline and normalised to shares p₁…p₁₁, which sum to 1. These shares are shown in **panel B**.

## 3. Index calculation

The *Interdisciplinary Index* is the **Rao–Stirling diversity**:

$$\Delta = \sum_{i \neq j} p_i \, p_j \, d_{ij} \;=\; \mathbf{p}^\top D\,\mathbf{p}$$

- **p** is the industry's discipline-share vector (Section 2).
- **d_ij** is the cognitive distance between disciplines *i* and *j*, scaled to [0, 1].

The index rises with three things:

- **Variety:** how many disciplines are present.
- **Balance:** how evenly the employment is spread across them.
- **Disparity:** how far apart those disciplines are.

It is 0 when all staff belong to a single discipline.

**Distance matrix D.** The 11 disciplines were placed on a 2-D circle that approximates the layout of the global map of science (Rafols, Porter & Leydesdorff 2010): mathematics → physics → engineering → chemistry → biology → medicine → social sciences → law → economics → design → computer science. d_ij is the Euclidean distance between two positions, divided by the largest pairwise distance.

| Discipline | x | y |
|---|---|---|
| Math/Statistics | 0.00 | 1.00 |
| Physics | 0.50 | 0.90 |
| Engineering | 0.88 | 0.48 |
| Chemistry | 1.00 | −0.05 |
| Biology | 0.72 | −0.62 |
| Medicine | 0.20 | −0.98 |
| Social sciences | −0.55 | −0.80 |
| Law/Regulation | −0.92 | −0.45 |
| Business/Economics | −1.00 | 0.02 |
| Design/Media | −0.88 | 0.48 |
| Computer science | −0.50 | 0.78 |

These coordinates are a stylised approximation chosen by hand. They are **not** estimated from citation data. **Panel A** shows Δ for each industry.

**Results (Δ):**

| Industry | Δ |
|---|---|
| R&D services | 0.589 |
| Pharma | 0.574 |
| Medical devices | 0.531 |
| Motor vehicles | 0.508 |
| Aerospace | 0.495 |
| Architecture/engineering services | 0.489 |
| Semiconductors | 0.468 |
| Food manufacturing | 0.435 |
| Management consulting | 0.301 |
| Software publishers | 0.232 |
| Legal services | 0.075 |

## 4. Limitations

1. **Occupation ≠ degree discipline.** A "software developer" in pharma may be a trained bioinformatician, and a "chemist" may be a biologist by training. Field-of-degree × industry data (e.g. U.S. Census ACS PUMS) would address this.
2. **Establishment-based classification.** NAICS 3254 covers drug manufacturers only. Much drug-development work happens in CROs, hospitals and biotech R&D firms, which fall under NAICS 5417 and other codes. Medicine and statistics are therefore likely under-represented for the full drug-discovery-and-development value chain.
3. **Business functions included.** Generic management and business roles all map to one discipline (Business/Economics), which ranges from about 9% (legal services) to 67% (consulting) of professional staff. Excluding them changes the ranking: food manufacturing and consulting then exceed pharma. See `results/index.csv`, column `index_core`.
4. **Hand-set mapping fractions and distance layout.** Both are judgement calls. The index measures the *composition* of the workforce, not the *integration* of disciplines within teams.
5. **U.S. data only, 2022/2023.** Swiss or European industry structures may differ.
6. **Rao–Stirling has known properties worth noting.** It mixes variety and balance into one term, and it can behave non-monotonically in balance (Leydesdorff, Wagner & Bornmann 2019; Rousseau 2018).

## References

- Stirling A (2007). A general framework for analysing diversity in science, technology and society. *J R Soc Interface* 4:707–719.
- Rafols I, Meyer M (2010). Diversity and network coherence as indicators of interdisciplinarity: case studies in bionanoscience. *Scientometrics* 82:263–287.
- Rafols I, Porter AL, Leydesdorff L (2010). Science overlay maps: a new tool for research policy and library management. *JASIST* 61:1871–1887.
- Leydesdorff L, Wagner CS, Bornmann L (2019). Interdisciplinarity as diversity in citation patterns among journals: Rao-Stirling diversity, relative variety, and the Gini coefficient. *J Informetrics* 13:255–269.
- U.S. Bureau of Labor Statistics. Occupational Employment and Wage Statistics, May 2022 and May 2023, industry-specific estimates.
