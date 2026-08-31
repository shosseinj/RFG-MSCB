# Audit of Our Quantitative Results

Evidence scope: Exp.45 seeds 42, 6543, and 7777. Verified aggregate values are the evidence package's arithmetic means and sample standard deviations (`ddof=1`), rounded to four decimal places. `paper_evidence_exp45/` is treated as authoritative for our results and complexity.

| Location | Dataset | Metric | Current value | Verified Exp45 value | Status |
|---|---|---|---|---|---|
| `sections/04_experiments.tex:206-213`, legacy all-dataset table, `Our9388` | Kvasir-SEG | mDice | 0.9349 | 0.9313 $\pm$ 0.0044 | STALE |
| Same | Kvasir-SEG | mIoU | 0.8777 | 0.8826 $\pm$ 0.0062 | STALE |
| Same | CVC-ClinicDB | mDice | 0.9492 | 0.9370 $\pm$ 0.0024 | STALE |
| Same | CVC-ClinicDB | mIoU | 0.9033 | 0.8877 $\pm$ 0.0038 | STALE |
| Same | CVC-300 | mDice | 0.9033 | 0.8821 $\pm$ 0.0016 | STALE |
| Same | CVC-300 | mIoU | 0.8252 | 0.8104 $\pm$ 0.0018 | STALE |
| Same | CVC-ColonDB | mDice | 0.7974 | 0.7944 $\pm$ 0.0089 | STALE |
| Same | CVC-ColonDB | mIoU | 0.6920 | 0.7142 $\pm$ 0.0086 | STALE |
| Same | ETIS-LaribPolypDB | mDice | 0.8869 | 0.7870 $\pm$ 0.0113 | STALE |
| Same | ETIS-LaribPolypDB | mIoU | 0.7967 | 0.7071 $\pm$ 0.0120 | STALE |
| `sections/04_experiments.tex:208-209`, legacy all-dataset table, `Ours` | Kvasir-SEG | mDice | 0.9258 | 0.9313 $\pm$ 0.0044 | STALE |
| Same | Kvasir-SEG | mIoU | 0.8641 | 0.8826 $\pm$ 0.0062 | STALE |
| Same | CVC-ClinicDB | mDice | 0.9531 | 0.9370 $\pm$ 0.0024 | STALE |
| Same | CVC-ClinicDB | mIoU | 0.9104 | 0.8877 $\pm$ 0.0038 | STALE |
| Same | CVC-300 | mDice | 0.9149 | 0.8821 $\pm$ 0.0016 | STALE |
| Same | CVC-300 | mIoU | 0.8432 | 0.8104 $\pm$ 0.0018 | STALE |
| Same | CVC-ColonDB | mDice | 0.8334 | 0.7944 $\pm$ 0.0089 | STALE |
| Same | CVC-ColonDB | mIoU | 0.7375 | 0.7142 $\pm$ 0.0086 | STALE |
| Same | ETIS-LaribPolypDB | mDice | 0.8739 | 0.7870 $\pm$ 0.0113 | STALE |
| Same | ETIS-LaribPolypDB | mIoU | 0.7761 | 0.7071 $\pm$ 0.0120 | STALE |
| `sections/04_experiments.tex:210-213`, rows `Ours-93.04` and `Ours-93.66` | All five | Available mDice/mIoU entries | Partial single-run values | Three-seed values listed above | CONFLICT |
| Kvasir-SEG comparison table, `sections/04_experiments.tex:278-279` | Kvasir-SEG | mDice | 0.935 | 0.9313 $\pm$ 0.0044 | STALE |
| Same | Kvasir-SEG | mIoU | 0.879 | 0.8826 $\pm$ 0.0062 | STALE |
| Same | Kvasir-SEG | Weighted F-measure | 0.901 | 0.9113 $\pm$ 0.0053 | STALE |
| Same | Kvasir-SEG | S-measure | 0.935 | 0.9331 $\pm$ 0.0026 | STALE |
| Same | Kvasir-SEG | Mean E-measure | 0.952 | 0.9602 $\pm$ 0.0027 | STALE |
| Same | Kvasir-SEG | Max E-measure | 0.963 | 0.9665 $\pm$ 0.0026 | STALE |
| Same | Kvasir-SEG | MAE | 0.025 | 0.0240 $\pm$ 0.0007 | STALE |
| CVC-ClinicDB comparison table, `sections/04_experiments.tex:340-341` | CVC-ClinicDB | mDice | 0.951 | 0.9370 $\pm$ 0.0024 | STALE |
| Same | CVC-ClinicDB | mIoU | 0.906 | 0.8877 $\pm$ 0.0038 | STALE |
| Same | CVC-ClinicDB | Weighted F-measure | 0.931 | 0.9254 $\pm$ 0.0027 | STALE |
| Same | CVC-ClinicDB | S-measure | 0.954 | 0.9466 $\pm$ 0.0012 | STALE |
| Same | CVC-ClinicDB | Mean E-measure | 0.983 | 0.9776 $\pm$ 0.0007 | STALE |
| Same | CVC-ClinicDB | Max E-measure | 0.990 | 0.9825 $\pm$ 0.0007 | STALE |
| Same | CVC-ClinicDB | MAE | 0.009 | 0.0109 $\pm$ 0.0003 | STALE |
| ETIS-LaribPolypDB comparison table, `sections/04_experiments.tex:402-403` | ETIS-LaribPolypDB | mDice | 0.887 | 0.7870 $\pm$ 0.0113 | STALE |
| Same | ETIS-LaribPolypDB | mIoU | 0.797 | 0.7071 $\pm$ 0.0120 | STALE |
| Same | ETIS-LaribPolypDB | Weighted F-measure | 0.730 | 0.7532 $\pm$ 0.0074 | STALE |
| Same | ETIS-LaribPolypDB | S-measure | 0.873 | 0.8780 $\pm$ 0.0037 | STALE |
| Same | ETIS-LaribPolypDB | Mean E-measure | 0.883 | 0.9024 $\pm$ 0.0024 | STALE |
| Same | ETIS-LaribPolypDB | Max E-measure | 0.913 | 0.9157 $\pm$ 0.0028 | STALE |
| Same | ETIS-LaribPolypDB | MAE | 0.014 | 0.0146 $\pm$ 0.0008 | STALE |
| CVC-ColonDB comparison table, `sections/04_experiments.tex:464` | CVC-ColonDB | mDice | 79.74 (mixed percentage scale) | 0.7944 $\pm$ 0.0089 | CONFLICT |
| Same | CVC-ColonDB | mIoU | 69.20 (mixed percentage scale) | 0.7142 $\pm$ 0.0086 | CONFLICT |
| Same | CVC-ColonDB | Weighted F-measure | 0.759 | 0.7715 $\pm$ 0.0066 | STALE |
| Same | CVC-ColonDB | S-measure | 0.869 | 0.8612 $\pm$ 0.0060 | STALE |
| Same | CVC-ColonDB | Mean E-measure | 0.885 | 0.8983 $\pm$ 0.0040 | STALE |
| Same | CVC-ColonDB | Max E-measure | 0.903 | 0.9050 $\pm$ 0.0038 | STALE |
| Same | CVC-ColonDB | MAE | 0.035 | 0.0349 $\pm$ 0.0010 | STALE |
| CVC-300 comparison table, `sections/04_experiments.tex:525-526` | CVC-300 | mDice | 0.916 | 0.8821 $\pm$ 0.0016 | STALE |
| Same | CVC-300 | mIoU | 0.845 | 0.8104 $\pm$ 0.0018 | STALE |
| Same | CVC-300 | Weighted F-measure | 0.848 | 0.8571 $\pm$ 0.0010 | STALE |
| Same | CVC-300 | S-measure | 0.939 | 0.9281 $\pm$ 0.0030 | STALE |
| Same | CVC-300 | Mean E-measure | 0.951 | 0.9558 $\pm$ 0.0047 | STALE |
| Same | CVC-300 | Max E-measure | 0.969 | 0.9706 $\pm$ 0.0015 | STALE |
| Same | CVC-300 | MAE | 0.007 | 0.0074 $\pm$ 0.0003 | STALE |
| `sections/04_experiments.tex:62` | Architecture-level | Trainable parameters | 30,057,415 | 30,057,415 | VERIFIED |
| `sections/03_method.tex:484-496` | Architecture-level | Trainable parameters | 30,057,415 (30.06 M) | 30,057,415 (30.06 M) | VERIFIED |
| `sections/03_method.tex:31` and `sections/04_experiments.tex:33` | Architecture-level | Input size | 352 x 352 | 352 x 352 | VERIFIED |
| `manuscript.tex:135`, uncaptained legacy comparison table | NOT AVAILABLE | Dice | 93.89 | Dataset is not identified; no valid Exp45 mapping | NOT AVAILABLE |
| Same | NOT AVAILABLE | IoU | 88.66 | Dataset is not identified; no valid Exp45 mapping | NOT AVAILABLE |
| Same | Architecture-level | Parameters | 38.5 M | 30.057415 M | STALE |
| Same | Architecture-level | Input size | 352 x 352 | 352 x 352 | VERIFIED |
| `manuscript.tex:306-310`, first uncaptained all-dataset table | All five | mDice/mIoU | Multiple partial single-run rows | Verified three-seed vectors listed above | CONFLICT |
| `manuscript.tex:388-402`, second uncaptained all-dataset table | All five | mDice/mIoU | Multiple partial single-run rows | Verified three-seed vectors listed above | CONFLICT |
| `manuscript.tex:460`, complexity table | Architecture-level | Parameters | 29.60 M | 30.057415 M (30.06 M) | STALE |
| Same | Architecture-level | GFLOPs | 14.57 | 27.818488992 at 1 x 3 x 352 x 352 | STALE |

## Verified Exp45 values

| Dataset | mDice | mIoU | Weighted F | S-measure | Mean E | Max E | MAE |
|---|---:|---:|---:|---:|---:|---:|---:|
| Kvasir-SEG | 0.9313 $\pm$ 0.0044 | 0.8826 $\pm$ 0.0062 | 0.9113 $\pm$ 0.0053 | 0.9331 $\pm$ 0.0026 | 0.9602 $\pm$ 0.0027 | 0.9665 $\pm$ 0.0026 | 0.0240 $\pm$ 0.0007 |
| CVC-ClinicDB | 0.9370 $\pm$ 0.0024 | 0.8877 $\pm$ 0.0038 | 0.9254 $\pm$ 0.0027 | 0.9466 $\pm$ 0.0012 | 0.9776 $\pm$ 0.0007 | 0.9825 $\pm$ 0.0007 | 0.0109 $\pm$ 0.0003 |
| CVC-300 | 0.8821 $\pm$ 0.0016 | 0.8104 $\pm$ 0.0018 | 0.8571 $\pm$ 0.0010 | 0.9281 $\pm$ 0.0030 | 0.9558 $\pm$ 0.0047 | 0.9706 $\pm$ 0.0015 | 0.0074 $\pm$ 0.0003 |
| CVC-ColonDB | 0.7944 $\pm$ 0.0089 | 0.7142 $\pm$ 0.0086 | 0.7715 $\pm$ 0.0066 | 0.8612 $\pm$ 0.0060 | 0.8983 $\pm$ 0.0040 | 0.9050 $\pm$ 0.0038 | 0.0349 $\pm$ 0.0010 |
| ETIS-LaribPolypDB | 0.7870 $\pm$ 0.0113 | 0.7071 $\pm$ 0.0120 | 0.7532 $\pm$ 0.0074 | 0.8780 $\pm$ 0.0037 | 0.9024 $\pm$ 0.0024 | 0.9157 $\pm$ 0.0028 | 0.0146 $\pm$ 0.0008 |

## Claims and stale occurrences elsewhere

- `sections/01_introduction.tex` contains no numerical performance result to update.
- `sections/02_related_work.tex` contains no numerical performance result to update.
- `sections/03_method.tex` and the revised implementation details report the verified 30,057,415 parameter count.
- `sections/05_discussion.tex` and `sections/06_conclusion.tex` contain no numerical result claims.
- The uncaptained legacy tables embedded directly in `manuscript.tex` report stale or dataset-unidentifiable results. They must not remain as quantitative evidence in the compiled paper.
- `manuscript_raw.tex` is not included by the build but retains obsolete 29.60/29.61/38.5 M complexity values and stale single-run results. It should be treated as an archival draft, not a manuscript source.

## Complexity audit

- Trainable parameters: **30,057,415 (verified)**.
- Total parameters: **30,057,415 (verified)**.
- Complexity: **27.818488992 GFLOPs (verified)** under the project convention `FLOPs = 2 x MACs`.
- Complexity input: **1 x 3 x 352 x 352 (verified)**.
- Hardware/GPU model: **NOT AVAILABLE / NOT VERIFIED** in the final result package.
