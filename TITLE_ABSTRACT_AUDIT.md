# Title and Abstract Audit

## Scope and evidence rule

The title and abstract were drafted from the compiled manuscript and the local evidence packages. FAFEM and MSCB are treated as prior components. The claimed contribution is limited to RFG-MSCB: reuse of the bottleneck FAFEM descriptor for sample-specific MSCB branch weighting, bounded residual guidance that preserves the ordinary MSCB path, and cross-level bottleneck-to-Stage-3 guidance.

External literature was used only to check positioning and terminology already represented in `sections/01_introduction.tex`, `sections/02_related_work.tex`, and `references.bib`. No externally sourced result was added to the abstract.

## Candidate titles

1. **Cross-Level Residual Frequency-Guided Multi-Scale Refinement with a ConvNeXt Encoder for Polyp Segmentation** (12 words)
   - Balances the new coupling, its cross-level structure, the encoder family, and the application without attributing FAFEM or MSCB to this work.
2. **Residual Frequency-Guided Multi-Scale Branch Adaptation for ConvNeXt-Based Polyp Segmentation** (10 words)
   - Concise and centered on the sample-adaptive multi-branch mechanism.
3. **Bottleneck-to-Decoder Frequency Guidance for Residual Multi-Scale Refinement in Polyp Segmentation** (11 words)
   - Emphasizes the direction of the cross-level guidance.
4. **RFG-MSCB: Bounded Residual Frequency Guidance for Multi-Scale Polyp Segmentation** (10 words)
   - Names the proposed block and foregrounds the bounded residual formulation.
5. **Frequency-Conditioned Multi-Kernel Branch Weighting with Residual Guidance for Polyp Segmentation** (10 words)
   - Describes the operational mechanism without relying on module acronyms.
6. **Reusing Bottleneck Frequency Descriptors for Stage-3 Multi-Scale Polyp Segmentation Refinement** (11 words)
   - Makes descriptor reuse and placement explicit while avoiding a novelty claim for FAFEM.
7. **ConvNeXt-Based Polyp Segmentation with Cross-Level Frequency-Guided Multi-Scale Refinement** (9 words)
   - Leads with the architecture and application; slightly shorter than the preferred range.
8. **Preserving Ordinary Multi-Scale Paths through Bounded Frequency-Guided Residual Adaptation for Polyp Segmentation** (12 words)
   - Highlights preservation of the prior MSCB pathway, although it is less concise than the leading options.

## Ranked selections

1. **Best overall:** Cross-Level Residual Frequency-Guided Multi-Scale Refinement with a ConvNeXt Encoder for Polyp Segmentation
   - Most complete balance of novelty, architecture, and task; it does not imply that FAFEM or MSCB was invented here.
2. **Best concise title:** RFG-MSCB: Bounded Residual Frequency Guidance for Multi-Scale Polyp Segmentation
   - Compactly names the contribution and its defining constraint.
3. **Best technically descriptive title:** Bottleneck-to-Decoder Frequency Guidance for Residual Multi-Scale Refinement in Polyp Segmentation
   - Most clearly communicates the cross-level information path.

## Final recommended title

**Cross-Level Residual Frequency-Guided Multi-Scale Refinement with a ConvNeXt Encoder for Polyp Segmentation**

## Final abstract

Accurate colorectal polyp segmentation remains challenging because lesions vary in scale, morphology, contrast, and boundary appearance. Conventional multi-scale convolution blocks aggregate different receptive fields without explicitly using sample-specific frequency information from deep semantic features. We present a ConvNeXt-Tiny U-shaped framework that builds on a bottleneck Frequency-Aware Feature Enhancement Module (FAFEM) and a Multi-Scale Convolution Block (MSCB), and introduce a Residual Frequency-Guided MSCB (RFG-MSCB). RFG-MSCB reuses the low- and high-frequency descriptor produced by FAFEM to assign sample-dependent weights to the MSCB multi-kernel branches at the Stage-3 encoder--decoder fusion. The guided response is introduced as a bounded residual deviation from ordinary MSCB aggregation, preserving the conventional multi-scale path as a reference. We evaluated the model on Kvasir-SEG, CVC-ClinicDB, CVC-300, CVC-ColonDB, and ETIS-LaribPolypDB over three random seeds. The model obtained mDice/mIoU of 0.9313 $\pm$ 0.0044/0.8826 $\pm$ 0.0062 on Kvasir-SEG and 0.9370 $\pm$ 0.0024/0.8877 $\pm$ 0.0038 on CVC-ClinicDB. On the three external datasets, mDice ranged from 0.7870 $\pm$ 0.0113 on ETIS-LaribPolypDB to 0.8821 $\pm$ 0.0016 on CVC-300. In the three-seed ablation, adding residual frequency-guided coupling to FAFEM + MSCB increased Kvasir-SEG mDice from 0.9304 $\pm$ 0.0022 to 0.9313 $\pm$ 0.0044, an observed difference of +0.08 percentage points. These results support bounded cross-level frequency guidance as a viable refinement strategy, while performance degradation on the more challenging external datasets indicates remaining generalization limitations.

**Word count:** 232 words in the compiled PDF text, counting hyphenated compounds as single tokens.

## Numerical claim ledger

| Abstract value | Meaning | Evidence source |
|---|---|---|
| Three random seeds | Seeds 42, 6543, and 7777; sample SD uses `ddof=1` | `paper_evidence_exp45/EXP45_THREE_SEED_RESULTS.md`, lines 3--11; `EXP45_THREE_SEED_RESULTS.csv` aggregate rows |
| 0.9313 $\pm$ 0.0044 | Kvasir-SEG mDice | `paper_evidence_exp45/EXP45_THREE_SEED_RESULTS.md`, line 65; CSV aggregate rows 163--164 |
| 0.8826 $\pm$ 0.0062 | Kvasir-SEG mIoU | `paper_evidence_exp45/EXP45_THREE_SEED_RESULTS.md`, line 66; CSV aggregate rows 165--166 |
| 0.9370 $\pm$ 0.0024 | CVC-ClinicDB mDice | `paper_evidence_exp45/EXP45_THREE_SEED_RESULTS.md`, line 29; CSV aggregate rows 121--122 |
| 0.8877 $\pm$ 0.0038 | CVC-ClinicDB mIoU | `paper_evidence_exp45/EXP45_THREE_SEED_RESULTS.md`, line 30; CSV aggregate rows 123--124 |
| 0.7870 $\pm$ 0.0113 | ETIS-LaribPolypDB mDice | `paper_evidence_exp45/EXP45_THREE_SEED_RESULTS.md`, line 53; CSV aggregate rows 149--150 |
| 0.8821 $\pm$ 0.0016 | CVC-300 mDice | `paper_evidence_exp45/EXP45_THREE_SEED_RESULTS.md`, line 17; CSV aggregate rows 107--108 |
| 0.9304 $\pm$ 0.0022 | FAFEM + MSCB Kvasir-SEG mDice | `paper_evidence_ablation/ABLATION_RESULTS.csv`, Exp37 Kvasir-SEG mDice for seeds 42, 6543, and 7777; independently recomputed mean 0.930440318783 and sample SD 0.002233812292; mean also appears in `ABLATION_MASTER_SUMMARY.md`, line 38 |
| 0.9313 $\pm$ 0.0044 | FAFEM + RFG-MSCB Kvasir-SEG mDice | `paper_evidence_ablation/ABLATION_RESULTS.csv`, Exp45 Kvasir-SEG mDice for the same three seeds; independently recomputed mean 0.931284016569 and sample SD 0.004422847521; `EXP45_THREE_SEED_RESULTS.md`, line 65 |
| +0.08 percentage points | Difference between the preceding three-seed means | Recomputed raw difference: 0.000843697786, or 0.0843697786 percentage points, rounded to +0.08 pp |

No parameter count or FLOP value is used in the abstract because the principal experimental and ablation findings are more informative within the target length.

## Claims requiring caution

- The ablation evidence files conflict. `ABLATION_AUDIT.md`, lines 171--174, uses an Exp37 mDice of 0.929373 and reports +0.19 pp, but `ABLATION_RESULTS.csv` and the raw-evidence-based `ABLATION_MASTER_SUMMARY.md` give an Exp37 three-seed mean of 0.930440. The abstract uses the independently recomputed CSV value and +0.08 pp. Existing manuscript sections that state +0.19 pp require a separate consistency correction.
- `ABLATION_AUDIT.md` also contains protocol statements at lines 34--43 that conflict with the final ConvNeXt-Tiny, 352 x 352, batch-24 protocol documented in `ABLATION_MASTER_SUMMARY.md` and the final experiment evidence. Those statements were not used.
- The final-model results are descriptive three-seed means; no significance test supports a claim of statistical significance.
- CVC-ColonDB and ETIS-LaribPolypDB performance is lower than on the held-out datasets. The abstract therefore reports remaining generalization limitations rather than robust generalization.
- The mechanistic interpretation is supported by the combined ablation only. Residualization, initialization strength, and frequency conditioning were not individually disentangled.
- FAFEM's exact original citation remains unresolved in `sections/02_related_work.tex`; the abstract identifies it as a component the method builds on and makes no originality claim for it.
