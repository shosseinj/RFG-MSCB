# Introduction Audit Against the Final Model

## Scope and overall assessment

This audit compares `sections/01_introduction.tex` with the stated final architecture: ConvNeXt-Tiny encoder, bottleneck FAFEM, lightweight residual bottleneck, Stage-3 `SimpleFusion`, the proposed Residual Frequency-Guided MSCB (RFG-MSCB), and standard remaining decoder stages. The current Introduction still describes an older MSC/BSEI/detail-fusion/deep-supervision model. Lines 74--108 therefore require substantial architectural correction when the Introduction is revised. This document identifies changes but does not rewrite the Introduction.

## 1. Sentences inconsistent with the final architecture

### Critical inconsistencies

| Lines | Current sentence or claim | Problem relative to final model | Required direction for later revision |
|---:|---|---|---|
| 74--75 | “This study proposes a multi-scale and boundary-sensitive ConvNeXt-UNet...” | “Boundary-sensitive” points to the removed BSEI/detail mechanisms and does not describe the final novelty. | Frame the model as frequency-guided, multi-scale decoder refinement based on cross-level bottleneck guidance. |
| 77--79 | “A lightweight residual bottleneck and a Multi-Scale Context module are applied to the deepest encoder feature...” | The lightweight residual bottleneck exists, but MSC is disabled and absent. FAFEM, which is applied at the bottleneck before the residual bottleneck, is omitted. | Retain the lightweight residual bottleneck; replace the MSC description with accurate bottleneck FAFEM placement and descriptor extraction. Do not claim FAFEM as new. |
| 80--82 | “...a Boundary-Sensitive Enhancement and Integration module refines the concatenated encoder and decoder features...” | BSEI is absent. Stage-3 uses `SimpleFusion`; the remaining decoder stages also use standard fusion. | Describe Stage-3 `SimpleFusion` followed by RFG-MSCB; do not claim edge-response attention. |
| 82--85 | “...a shallow Detail Branch... A Gated Detail Fusion module...” | Neither Detail Branch nor Gated Detail Fusion is present. | Remove both claims entirely. |
| 85--86 | “Three auxiliary output heads provide intermediate supervision...” | Deep supervision is disabled; no auxiliary heads are instantiated. | Remove the sentence. |
| 86--87 | “...approximately 29.61 million trainable parameters.” | This is stale for the final model. The final architecture audit reports 30,057,415 trainable parameters (about 30.06 M). | Replace only after reconfirming the count from the final evaluation artifact used for the paper. |

### Motivation-to-architecture mismatches

- **Lines 31--35:** The criticism that ordinary skip connections transfer redundant texture/background information “without explicit feature selection” sets up an attention/gating remedy, but the final model uses `SimpleFusion` rather than gated or boundary-sensitive skip selection. This can remain as broad background only if it is not presented as the specific problem solved by the proposed model.
- **Lines 65--69:** The second and third stated limitations emphasize boundary enhancement and shallow spatial-detail control. The final model contains no dedicated boundary module, Detail Branch, or Gated Detail Fusion. These limitations should be replaced or subordinated to the actual gap: fixed multi-scale decoder branches do not adapt their scale contributions using image-specific frequency information, and bottleneck frequency cues are normally not reused to guide decoder refinement.
- **Lines 42--51:** The global-context/transformer paragraph leads naturally to the removed MSC module, not to RFG-MSCB. It needs a clearer transition from global semantic context to efficient convolutional multi-scale processing and frequency-aware, sample-adaptive branch selection.

## 2. Outdated claimed contributions

1. **Contribution 1 (lines 91--93): partially defensible but generic.** A ConvNeXt-Tiny U-shaped network with a lightweight decoder is present, but this combination alone is not the main novelty. It should be background/system context rather than the leading invention unless the paper establishes a distinct architectural contribution beyond known ConvNeXt-U-Net combinations.
2. **Contribution 2 (lines 95--97): obsolete.** The claimed bottleneck Multi-Scale Context module is not in the final model.
3. **Contribution 3 (lines 99--101): obsolete.** BSEI and its spatial edge-response modulation are not in the final model.
4. **Contribution 4 (lines 103--105): obsolete.** Detail Branch and Gated Detail Fusion are not in the final model.
5. **Contribution 5 (lines 107--108): obsolete.** Deep-supervision heads are not enabled.
6. **Contribution 6 (lines 110--112): potentially defensible as an evaluation contribution.** Keep only if the Experiments section actually reports all five named datasets and both claimed protocols. It is evidence of evaluation breadth, not architectural novelty.

The current contribution list completely omits the implemented novelty: descriptor-conditioned MSCB branch weighting, bounded residual guidance, and bottleneck-to-Stage-3 cross-level guidance.

## 3. Claims that require citations

The audit distinguishes claims needing external literature from claims that should instead be supported by this paper's methods/results.

### External citations needed or needing stronger placement

- **Lines 3--7:** Polyps may progress to malignancy; early detection/removal and colonoscopy's clinical role. These are clinical claims and need authoritative clinical/guideline or epidemiological citations.
- **Lines 7--12:** Reliability of colonoscopic visual inspection is affected by operator experience, fatigue, and imaging conditions; computer-aided segmentation can assist examination. Cite clinical studies or reviews. Avoid implying demonstrated clinical benefit from segmentation alone unless supported by clinical evidence.
- **Lines 14--24:** Variability in polyp appearance and interference from reflections, blur, bubbles, shadows, fecal material, and instruments. Cite polyp-segmentation surveys, dataset papers, or empirical studies documenting these challenges.
- **Lines 26--36:** U-shaped architectures' prevalence and the benefits/risks of skip connections and downsampling. Lines 36--40 cite U-Net/UNet++, but the broader claims in lines 26--35 also need suitable support, especially the assertion about redundant texture/background transfer.
- **Lines 42--51:** Use of transformer/hybrid architectures, their global-context capability, computational cost, and possible need for local-boundary mechanisms. TransUNet and Polyp-PVT are cited, but “considerable computational complexity” and the boundary limitation require direct comparative or review support rather than assertion.
- **Lines 53--60:** The listed ConvNeXt design elements and competitive representation capacity appropriately point to citation `[5]`; ensure `[5]` is the original ConvNeXt source and use the project's final citation mechanism consistently.
- **Lines 62--72:** The statements that lesion-scale variation “requires” multi-receptive-field context and that practical inference efficiency is important should be supported by relevant segmentation literature. Prefer calibrated wording (“motivates” or “may benefit from”) unless necessity is directly established.
- **Future RFG-MSCB motivation:** Any claim that fixed MSCB scale branches are suboptimal, that frequency composition should determine receptive-field weighting, or that bottleneck frequency information improves Stage-3 decoding requires citations to related frequency-aware segmentation/adaptive multi-scale work plus direct ablation evidence from this study.

### Internal evidence required rather than external citations

- The final trainable-parameter count should be tied to the exact evaluated checkpoint/configuration.
- Any claim that RFG-MSCB improves accuracy, generalization, boundary quality, efficiency, or robustness must be limited to metrics actually reported in the ablation and cross-dataset experiments.
- Any statement that residual bounded guidance stabilizes optimization or preserves ordinary MSCB behavior must distinguish a mathematical property from an empirical benefit. The identity with ordinary MSCB at zero strength or uniform weights follows from the formula; improved training stability requires experimental evidence.
- The five-dataset and in-/cross-dataset evaluation claim must match the actual dataset splits and tables.

## 4. Generic or weak motivation paragraphs

### Lines 3--12: broad clinical opening

The paragraph is conventional and lengthy relative to its role. It moves from polyp malignancy to colonoscopy variability to computer-aided segmentation without quantifying clinical importance or defining the technical problem. A revision should compress the generic clinical background and use one or two authoritative citations, then move quickly to the segmentation challenge addressed by the model.

### Lines 14--24: useful challenge inventory, but unfocused

The list of appearance artifacts is relevant, yet it treats scale, texture, boundary ambiguity, and acquisition artifacts as equally central. The final architecture specifically targets adaptive multi-scale processing conditioned on frequency information. The paragraph should prioritize lesion-scale variability and frequency/content heterogeneity, while retaining boundary ambiguity only as a downstream segmentation difficulty rather than promising a dedicated boundary module.

### Lines 26--40: U-Net background sets up a removed solution

The paragraph motivates selective skip refinement and deep supervision, neither of which exists in the final model. It is too detailed about UNet++ relative to the proposed mechanism. Retain a shorter explanation of hierarchical encoder-decoder fusion and identify the actual unresolved issue: ordinary decoder refinement and fixed multi-scale branches are not conditioned on image-specific frequency characteristics.

### Lines 42--51: weak connection to the final method

The transformer/global-context discussion is not inherently wrong, but the logical bridge to RFG-MSCB is missing. As written, it motivates global-context modeling and local boundary recovery. Recast it as a trade-off: global/contextual capacity is valuable, but an efficient convolutional model also needs adaptive local-to-broad receptive-field allocation.

### Lines 53--60: relevant but descriptive

This paragraph justifies ConvNeXt-Tiny but does not connect its hierarchical features to the proposed guidance path. It can be shortened and ended with the specific opportunity: the deepest ConvNeXt representation supplies semantic/frequency information that can guide decoder-scale refinement.

### Lines 62--72: central gap paragraph is outdated

This should become the strongest motivation paragraph, but its three limitations correspond to MSC, BSEI, and detail fusion. Replace them with a precise gap statement:

1. standard multi-scale convolution blocks aggregate fixed branches rather than adapting their relative influence per image;
2. bottleneck frequency information is usually consumed locally instead of guiding an earlier decoder stage; and
3. fully replacing ordinary MSCB with learned guidance may disturb a stable reused baseline, motivating bounded residual interpolation.

Claims about what prior methods “usually” do must be verified by the Related Work review and cited.

## 5. Suggested logical flow for the revised Introduction

1. **Clinical and technical problem:** Briefly establish why accurate polyp segmentation matters and identify scale variation, weak contrast, and heterogeneous frequency/texture content as the relevant challenges.
2. **Encoder-decoder background:** Explain why U-shaped hierarchical models and ConvNeXt-Tiny are suitable, while avoiding claims that the final model performs explicit boundary gating or deep supervision.
3. **Multi-scale and frequency-aware prior work:** Introduce MSCB and FAFEM as existing/reused approaches. State their roles accurately: MSCB provides parallel receptive fields; FAFEM separates/enhances low- and high-frequency information.
4. **Unresolved gap:** Fixed MSCB branch aggregation does not exploit a sample-specific frequency descriptor, and bottleneck frequency information is not carried across levels to guide Stage-3 decoder refinement. Establish this gap using citations rather than novelty by assertion.
5. **Proposed mechanism:** Introduce RFG-MSCB as the contribution: the bottleneck FAFEM descriptor weights the reused MSCB branches at Stage 3, while bounded residual interpolation retains the ordinary MSCB path and adds a controlled guided deviation.
6. **Architecture synopsis:** State only implemented components: ConvNeXt-Tiny encoder, bottleneck FAFEM, lightweight residual bottleneck, Stage-3 `SimpleFusion` followed by RFG-MSCB, standard remaining decoder stages, and final prediction head.
7. **Evidence and contributions:** Summarize the actual evaluation scope and give three or four non-overlapping, defensible contributions.

## 6. Proposed defensible contributions

1. **Frequency-conditioned multi-scale refinement:** We introduce RFG-MSCB, which uses the low-/high-frequency descriptor produced by an existing bottleneck FAFEM to generate sample-adaptive weights for the existing MSCB multi-kernel branches. This claims the coupling mechanism, not FAFEM or MSCB themselves.
2. **Bounded residual guidance:** We formulate the guided branch aggregation as `ordinary + s * (guided - ordinary)`, with bounded learned strength `s`, preserving the ordinary MSCB pathway as the reference and learning only a controlled frequency-conditioned deviation.
3. **Cross-level bottleneck-to-decoder guidance:** We transmit global bottleneck frequency information to the Stage-3 decoder refinement after `SimpleFusion`, connecting deep semantic/frequency evidence to an earlier, higher-resolution decoding stage while leaving the remaining decoder stages standard.
4. **Empirical validation:** We evaluate the resulting ConvNeXt-Tiny segmentation model on the five stated polyp datasets and use controlled ablations to isolate the effects of frequency guidance, residual guidance, and Stage-3 placement. Include this contribution only to the extent that the reported experiments directly support each clause.

## Novelty-language guardrails

- Do **not** write “we propose FAFEM,” “we introduce FAFEM,” “our FAFEM,” or equivalent invention language.
- Do **not** write “we propose MSCB,” “we introduce MSCB,” “our MSCB,” or imply ownership of its parallel-kernel/channel-shuffle topology.
- Use wording such as “we reuse/adopt FAFEM,” “we build on MSCB,” and “we introduce the residual frequency-guided coupling of FAFEM and MSCB.”
- Keep “RFG-MSCB” attached to the new guidance mechanism and formula, not to the reused MSCB operations alone.
- Avoid boundary-aware, edge-aware, detail-preserving, deep-supervision, or global-context-module claims unless another currently enabled component and direct evidence support them.
