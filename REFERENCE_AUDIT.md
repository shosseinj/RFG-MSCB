# Reference Audit

## Summary

The project now uses classic BibTeX with `unsrt.bst` and `references.bib`. The former manually typed References block was removed from `manuscript.tex` only after its usable entries were transferred. Prose and table citations were mapped contextually so that ambiguous numbers such as `[1]`--`[4]` were not replaced globally.

1. **Citation keys found after normalization:** 29 unique `\cite{...}` keys.
2. **BibTeX entries created:** 30. Twenty-nine are cited normally; the transferred HCA-Net placeholder is included with `\nocite{hcanet}`.
3. **Duplicate references merged:** 3 duplicate groups: MEGANet (`[47-1]`/`[9]`), Polyp-Mamba (`[48-1]`/`[8]`), and MSBP-Net (`[34-2]`/`[10]`). Each now has one BibTeX entry and one canonical key.
4. **Undefined BibTeX citation keys:** 0.
5. **Duplicate DOI values in `references.bib`:** 0.

## Citation keys renamed

### Core and related-work citations

| Old label | Canonical key |
|---|---|
| `[1]` (U-Net context) | `unet` |
| `[2]` (UNet++ context) | `unetpp` |
| `[3]` (TransUNet context) | `transunet` |
| `[4]` (Polyp-PVT context) | `polyppvt` |
| `[5]` | `convnext` |
| `[6]` | `hardnetmseg` |
| `[7]` | `pranet` |
| `[8]` (Polyp-Mamba context) | `polypmamba` |
| `[8]` (PraNet dataset-split context) | `pranet` |
| `[9]` | `meganet` |
| `[10]` | `msbpnet` |

### Temporary model labels

| Old label or ambiguous table label | Canonical key |
|---|---|
| `[20-1]` | `ctnet` |
| `[47-1]` | `meganet` |
| `[48-1]` | `polypmamba` |
| `[25-1]` | `mein` |
| `[25-2]` | `mfnet` |
| `[34-2]` | `msbpnet` |
| `[26-2]` | `cifformer` |
| `[29-2]` | `pfprnet` |
| `[11-3]` | `pranetv2` |
| `[2]` following CAFÉ-Net | `cafenet` |
| `[2]` following Polyp-LVT | `polyplvt` |
| `[2]` following MF-Net | `mfnet` |
| `[2]` following MSBP-Net | `msbpnet` |
| `[2]` following CIFFormer | `cifformer` |
| `[2]` following PFPRNet | `pfprnet` |
| `[1]` following MLB-Net | `mlbnet` |
| `[3]` following MSPN | `mspn` |
| `[4]` following DVFIP-Net | `dvfipnet` |

### Dataset and metric labels

| Old label | Canonical key |
|---|---|
| `[ho-32]` | `kvasirseg` |
| `[ho-33]` | `cvcclinicdb` |
| `[ho-34]` | `etis` |
| `[ho-35]` | `cvccolondb` |
| `[ho-36]` | `cvc300` |
| `[ho-f20]` | `smeasure` |
| `[ho-fan]`, `[ho-40]` | `emeasure` |
| `[ho-peraz]` | `saliencyfilters` |

## Incomplete references requiring manual verification

The following entries are valid BibTeX records containing only metadata explicitly available in the manuscript/table. Missing metadata was not invented:

- `cafenet`: title/model name and year only; authors and venue unknown.
- `polyplvt`: title/model name and year only; authors and venue unknown.
- `mlbnet`: title/model name and year only; authors and venue unknown.
- `hcanet`: title/model name only; authors, venue, and year unknown.
- `mspn`: manuscript-provided title and table year only; authors and venue unknown.
- `dvfipnet`: title/model name and year only; authors and venue unknown.

The table years for 2026 papers and the manuscript's future-publication metadata should be rechecked against the final publisher records before submission. PFPRNet was normalized to its verified final journal publication year, 2025, while its DOI retains 2024 in the identifier metadata.

## Unresolved citations and review items

- The Evaluation metrics paragraph contains an empty literal marker after “F-measure”: `F-measure{[}{]}`. The project provides no identifiable source for this marker. It was left unchanged rather than assigning an invented reference.
- Bracketed text beginning with “describe specific...” in the Experiments section is editorial placeholder text, not a bibliographic label. It was preserved unchanged.
- There are no unresolved `\cite{...}` keys and no `Citation ... undefined` warnings.

## Metadata verification

Identifiable metadata was reconciled against Crossref by title/author and, where available, DOI. TransUNet (`arXiv:2102.04306`) and HarDNet-MSEG (`arXiv:2101.07172`) were verified through the arXiv API because Crossref did not provide reliable records for those preprints. Access date: 2026-08-31.

The five required canonical entries are present:

- `unet`
- `unetpp`
- `transunet`
- `polyppvt`
- `convnext`

## Compile and resolution checks

- Command: `latexmk -pdf manuscript.tex`
- Result: success, exit code 0.
- BibTeX style/database: `unsrt.bst` / `references.bib`.
- Generated bibliography items: 30 (`manuscript.bbl`).
- Undefined-citation warnings: 0.
- BibTeX warnings: 0.
- LaTeX fatal errors: 0.
- Bibliography verified in the generated PDF; the PDF contains a References heading and all 30 entries.

Compilation initially exposed two stray Markdown code-fence lines surrounding the already present Introduction `itemize` list. Those two fence lines were removed as a LaTeX compatibility fix; no manuscript wording was changed.

## Exact files modified or created

### Manuscript sources and audit artifacts

- Modified: `manuscript.tex`
- Modified: `sections/01_introduction.tex` (removed two stray Markdown fence lines only)
- Modified: `sections/02_related_work.tex`
- Modified: `sections/04_experiments.tex`
- Created: `references.bib`
- Created: `REFERENCE_AUDIT.md`

### Build artifacts refreshed by compilation

- `manuscript.aux`
- `manuscript.bbl`
- `manuscript.blg`
- `manuscript.fdb_latexmk`
- `manuscript.fls`
- `manuscript.log`
- `manuscript.pdf`
- `manuscript.synctex.gz`
