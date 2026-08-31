# Computational-Complexity Table Audit

## Scope and decision rules

This audit covers every method in the manuscript's original complexity table. A value is retained in the manuscript only when it was directly recoverable from an original paper, an official author repository, publisher material, or verified local project evidence. Search-result snippets and the pre-existing manuscript table were used only for discovery, not verification.

Statuses mean:

- **VERIFIED:** the reported value and its source were directly inspected.
- **PARTIALLY VERIFIED:** some requested fields were verified, but one or more complexity fields or protocol details were unavailable.
- **NOT FOUND:** the requested complexity value was not found in accessible primary or official material.
- **NOT COMPARABLE:** a direct comparison with the project's 352 x 352, `FLOPs = 2 x MACs` measurement is not justified because resolution, variant, or operation-counting convention differs or is unknown.

No competitor value was converted between MACs and FLOPs. A source's term `GFLOPs` is preserved verbatim when its counting convention is not defined.

## Method-level audit

| Method | Year | Params (M) | MACs | GFLOPs | Input | FPS | Backbone / variant | Primary or official source and locator | Convention known? | Directly comparable? | Status |
|---|---:|---:|---:|---:|---|---|---|---|---|---|---|
| CTNet | 2024 | -- | -- | -- | 352 x 352 | -- | MiT-B3 | [Paper](https://doi.org/10.1109/TCYB.2024.3368154); [official repository](https://github.com/Fhujinwu/CTNet), `Training.py` default `trainsize=352`, `Test.py` default `testsize=352`, and `model/Mymodel13.py` MiT-B3 instantiation | No operation count found | No; only resolution is matched | **PARTIALLY VERIFIED**; complexity **NOT FOUND** |
| MEGANet (Res2Net-50) | 2024 | 44.19 | -- | -- | 352 x 352 | -- | Res2Net-50 | [WACV paper](https://openaccess.thecvf.com/content/WACV2024/html/Bui_MEGANet_Multi-Scale_Edge-Guided_Attention_Network_for_Weak_Boundary_Polyp_Segmentation_WACV_2024_paper.html), Table 2 (parameters) and Section 4.2 (input); [official repository](https://github.com/UARK-AICV/MEGANet) | No operation count found | Parameters only; exact variant is now named | **VERIFIED** for parameters/input; otherwise **PARTIALLY VERIFIED** |
| Polyp-Mamba | 2025 | -- | -- | -- | -- | -- | -- | [Publisher record](https://doi.org/10.1016/j.inffus.2024.102759). The old 49.5 M and 27.9 GFLOPs entries could not be confirmed in accessible primary or official material. | Unknown | No | **NOT FOUND; NOT COMPARABLE** |
| MEIN | 2025 | -- | -- | -- | -- | -- | -- | [Publisher record](https://doi.org/10.1016/j.neunet.2025.107553); no accessible primary complexity report or official repository was found | Unknown | No | **NOT FOUND; NOT COMPARABLE** |
| MF-Net | 2025 | -- | -- | -- | -- | -- | Pyramid visual transformer; exact variant unverified | [Publisher record](https://doi.org/10.1016/j.eswa.2025.127558); no accessible primary complexity report or official repository was found | Unknown | No | **NOT FOUND; NOT COMPARABLE** |
| MSBP-Net | 2026 | -- | -- | -- | -- | -- | -- | [Publisher record](https://doi.org/10.1016/j.patcog.2025.112101). The final volume year is 2026. The old 25.52 M and 12.86 GFLOPs entries could not be confirmed in accessible primary or official material. | Unknown | No | **NOT FOUND; NOT COMPARABLE** |
| CIFFormer | 2025 | -- | -- | -- | -- | -- | Pyramid visual transformer; exact variant unverified | [Publisher record](https://doi.org/10.1016/j.neucom.2025.130413); [official repository](https://github.com/lonlin404/CIFFormer). The old 32.44 M and 13.14 GFLOPs entries are not stated in the repository and were not directly recoverable from the accessible paper record. | Unknown | No | **PARTIALLY VERIFIED** for identity/repository; complexity **NOT FOUND; NOT COMPARABLE** |
| PFPRNet | 2025 | -- | -- | -- | -- | -- | Pre-trained Transformer-based encoder; exact variant unverified | [Publisher record](https://doi.org/10.1109/JBHI.2024.3500026); [PubMed](https://pubmed.ncbi.nlm.nih.gov/40030242/). The old 118.52 M and 39.39 GFLOPs entries were not exposed in accessible primary material. | Unknown | No | **PARTIALLY VERIFIED** for publication/architecture class; complexity **NOT FOUND; NOT COMPARABLE** |
| PraNet-V2 | 2025 | -- | -- | -- | 352 x 352 | 31 (PyTorch), 143 (Jittor) | Res2Net-50 | [arXiv](https://arxiv.org/abs/2504.10986), Section 3.1.2 (input); [official repository](https://github.com/ai4colonoscopy/PraNet-V2), `binary_seg/jittor/README.md` speed table. The repository also reports 29/117 FPS for the PVTv2-B2 variant. Hardware is not stated in the speed table. | No operation count found | No; FPS protocol is incomplete and no complexity count was found | **VERIFIED** for input/variant/repository FPS; complexity **NOT FOUND; NOT COMPARABLE** |
| MLB-Net | 2026 | -- | -- | -- | -- | -- | -- | [Publisher record](https://doi.org/10.1007/s10278-026-01909-z). The old 87.70 M entry could not be inspected in accessible primary material, and no official repository was found. | Unknown | No | **PARTIALLY VERIFIED** for publication identity; complexity **NOT FOUND; NOT COMPARABLE** |
| MSPN | 2026 | -- | -- | -- | -- | -- | -- | [Publisher record](https://doi.org/10.1109/ICASSP55912.2026.11461882). The old 28.56 M and 13.21 GFLOPs entries were not exposed in accessible primary material, and no official repository was found. | Unknown | No | **PARTIALLY VERIFIED** for publication identity; complexity **NOT FOUND; NOT COMPARABLE** |
| DVFIP-Net | 2026 | -- | -- | 19.37 | -- | -- | -- | [Publisher record](https://doi.org/10.1109/ACCESS.2026.3667956), abstract: “only 19.37 GFLOPs.” The old 46.62 M value was not visible in accessible primary material. | No; source says GFLOPs but does not define MAC treatment | No; input and convention are unavailable | **VERIFIED** for reported GFLOPs; overall **PARTIALLY VERIFIED; NOT COMPARABLE** |
| FAFEM + RFG-MSCB (Ours) | -- | 30.06 (exact: 30,057,415) | 13.909244496 GMACs | 27.818488992 (27.82 in table) | 1 x 3 x 352 x 352 | -- | ConvNeXt-Tiny encoder | `paper_evidence_exp45/EXP45_MODEL_COMPLEXITY.md`, backed by the three final `evaluation_summary.json` files and `evaluation_core.measure_complexity` | Yes: THOP MACs; project uses `FLOPs = 2 x MACs` | Reference row; competitor comparability remains source-dependent | **VERIFIED** |

## Table-design decision

The manuscript table uses **Method, Year, Input, Params (M), and Reported GFLOPs**. Backbone was omitted to avoid a wide table and because it could not be verified consistently. FPS was omitted because only PraNet-V2 had an official figure, and that figure lacks the hardware and timing protocol required for a defensible cross-method speed comparison.

`Reported GFLOPs` deliberately means the terminology used by each source. It is not a harmonized operation count. The manuscript caption and accompanying text state that unknown conventions and resolutions prevent direct ranking by GFLOPs.

## Audit outcome

- The original table was after the bibliography in `manuscript.tex`, where it was disconnected from both Method and Experiments.
- The replacement table is integrated into `Model Complexity` at the end of `sections/03_method.tex`.
- Unsupported competitor values are replaced by `--`; they are not silently carried forward.
- The exact project count is retained once in Method; rounded values are used in the publication table.
- Primary-source access limitations mean that absence in this audit is not evidence that a paper never reported a value. It means the value was not sufficiently verified for this manuscript revision.
