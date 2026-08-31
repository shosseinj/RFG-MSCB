# Related Work Audit

## 1. Outdated Paragraphs

- `sections/02_related_work.tex` lines 74--105 are outdated. They describe boundary-aware segmentation, MEGANet/MSBP-Net, and a proposed BSEI module. The final method does not include BSEI, explicit edge extraction, boundary labels, Laplacian/Sobel processing, or a boundary loss.
- `sections/02_related_work.tex` lines 107--131 are outdated. They describe a shallow Detail Branch and Gated Detail Fusion module. These modules are not part of the final architecture.
- `sections/02_related_work.tex` lines 136--153 are outdated. They position the method as combining multi-scale context, boundary-sensitive skip refinement, and selective detail fusion. The final novelty is instead the residual frequency-guided coupling between a bottleneck FAFEM descriptor and Stage-3 MSCB branches.
- `sections/02_related_work.tex` lines 63--72 are only partly aligned. The paragraph mentions frequency-oriented architectures but then says the method does not employ frequency decomposition; the final method does use FAFEM at the bottleneck and propagates its frequency descriptor to Stage 3.
- `sections/02_related_work.tex` lines 23--39 can be retained only as broad polyp-segmentation background. The final method should not be framed as solving noisy skip transfer through a special boundary/detail gate.

## 2. Missing Topics

- ConvNeXt as a modern convolutional hierarchical encoder and why it is a suitable alternative to transformer-heavy encoders.
- EMCAD/MSCB as prior work for efficient multi-scale convolutional attention decoding and multi-kernel branch processing.
- Frequency-aware feature processing in segmentation, including the distinction between local frequency enhancement and cross-level reuse of a frequency descriptor.
- Adaptive branch or receptive-field selection, especially selective-kernel style weighting of convolutional branches.
- Channel/frequency attention modules that use compact descriptors to reweight feature responses.
- The exact contribution: using a bottleneck FAFEM descriptor to adaptively weight Stage-3 MSCB branches, with bounded residual guidance and bottleneck-to-Stage-3 cross-level guidance.

## 3. Claims Needing Citations

- U-Net and UNet++ claims about encoder-decoder segmentation and skip-path redesign require `unet` and `unetpp`.
- Claims that efficient CNN polyp models can remain competitive require `hardnetmseg` and/or another verified efficient polyp source.
- Claims about reverse attention in polyp segmentation require `pranet`.
- Claims about transformer/global-context polyp segmentation require `transunet`, `polyppvt`, and recent transformer/hybrid polyp references where used.
- Claims about frequency-sensitive polyp segmentation require `polypmamba` or other verified frequency-aware polyp papers.
- Claims about edge/boundary-aware polyp segmentation require `meganet` and `msbpnet` if retained.
- Claims about MSCB and EMCAD require the verified EMCAD CVPR source.
- Claims about adaptive branch/receptive-field weighting require selective-kernel or related attention sources.
- Claims that RFG-MSCB improves accuracy, boundary quality, robustness, generalization, or efficiency must be supported by this paper's experiments and ablations, not by external citations alone.
- Claims that bounded residual guidance stabilizes optimization should be phrased as a design property unless training-stability evidence is reported.

## 4. Original Paper/Source for FAFEM

- Exact-source status: unresolved.
- Searches performed on 2026-08-31: Crossref title query for "Frequency-Aware Feature Enhancement Module"; Semantic Scholar API queries for exact phrase, `FAFEM segmentation`, and `Frequency-Aware Feature Enhancement segmentation`; arXiv API queries for the exact module phrase, `FAFEM`, and `Frequency-Aware Feature Enhancement`.
- Result: no exact scholarly source for a segmentation module named "Frequency-Aware Feature Enhancement Module" or acronym `FAFEM` was verified.
- Relevant but not exact: Crossref returned unrelated or non-medical matches such as `RGBT tracking via frequency-aware feature enhancement and unidirectional mixed attention` and `Frequency-aware Deep Dual-path Feature Enhancement Network for Image Dehazing`; arXiv returned unrelated/future non-polyp matches under broader frequency-aware wording.
- Action: do not add a FAFEM BibTeX entry until the authors provide the exact source title, DOI, arXiv ID, or publisher URL. In the manuscript, state only that FAFEM is adopted/reused and avoid invention language.

## 5. Original Paper/Source for MSCB / EMCAD

- Verified source: Md Mostafijur Rahman, Mustafa Munir, and Radu Marculescu, "EMCAD: Efficient Multi-Scale Convolutional Attention Decoding for Medical Image Segmentation," Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024, pages 11769--11779, DOI `10.1109/CVPR52733.2024.01118`.
- Relevance: this is the original verified EMCAD source and is the appropriate citation for MSCB when MSCB is described as prior work from EMCAD.
- Manuscript implication: do not claim MSCB as a contribution. The new contribution is the residual frequency-guided conditioning of MSCB branches using a FAFEM-derived descriptor.

## 6. Recent Relevant Polyp Segmentation Papers

- `ctnet`: CTNet, IEEE Transactions on Cybernetics, 2024, DOI `10.1109/TCYB.2024.3368154`.
- `meganet`: MEGANet, WACV 2024, DOI `10.1109/WACV57701.2024.00780`.
- `polypmamba`: Polyp-Mamba, Information Fusion, 2025, DOI `10.1016/j.inffus.2024.102759`.
- `mein`: Modeling Multi-Scale Uncertainty with Evidence Integration for Reliable Polyp Segmentation, Neural Networks, 2025, DOI `10.1016/j.neunet.2025.107553`.
- `mfnet`: Multi-Feature Fusion for Accurate Polyp Segmentation Using Pyramid Visual Transformers, Expert Systems with Applications, 2025, DOI `10.1016/j.eswa.2025.127558`.
- `msbpnet`: MSBP-Net, Pattern Recognition, verified as DOI `10.1016/j.patcog.2025.112101` with a 2026 volume/publication record in `references.bib`; manuscript tables may still label it as 2025 and should be checked against final publisher metadata.
- `cifformer`: CIFFormer, Neurocomputing, 2025, DOI `10.1016/j.neucom.2025.130413`.
- `pfprnet`: PFPRNet, IEEE Journal of Biomedical and Health Informatics, 2025, DOI `10.1109/JBHI.2024.3500026`.
- `pranetv2`: PraNet-V2, arXiv `2504.10986`, 2025 preprint.
- Several table-only entries in `references.bib` remain incomplete (`cafenet`, `polyplvt`, `mlbnet`, `hcanet`, `mspn`, `dvfipnet`) and should not be used for new prose claims until verified.

## 7. Possible Prior Work Close to RFG-MSCB

- Selective Kernel Networks adaptively select among convolutional kernels/receptive fields using global information. This is conceptually close to adaptive MSCB branch weighting, although it is not the same as cross-level frequency-guided decoder conditioning.
- Squeeze-and-Excitation Networks use global descriptors to reweight channels and form the broader precedent for descriptor-driven feature recalibration.
- FcaNet introduces frequency-channel attention, showing that frequency-domain/channel-frequency descriptors can guide attention weights.
- Polyp-Mamba uses multi-frequency perception and gated selection for polyp segmentation; this is a domain-specific frequency/gating prior that should be cited when discussing frequency-aware polyp segmentation.
- EMCAD/MSCB already provides efficient multi-scale convolutional decoding. RFG-MSCB must be presented as a coupling/modulation mechanism on top of prior MSCB, not as a new multi-scale block family from scratch.

## 8. Novelty Risks

- High risk if the paper says "we propose FAFEM" or "we introduce MSCB." Both should be treated as prior modules.
- Moderate risk from Selective Kernel Networks because they already adaptively weight multi-kernel branches. The distinction is that RFG-MSCB uses a frequency descriptor extracted at the bottleneck by FAFEM and transfers it to Stage 3, rather than learning branch weights only from the same local multi-branch feature.
- Moderate risk from FcaNet/frequency-channel attention because it links frequency descriptors and attention. The distinction is the target of guidance: MSCB branch weights in a polyp decoder, not only channel recalibration.
- Moderate risk from Polyp-Mamba because it combines multi-frequency perception and gated selection in polyp segmentation. The distinction is that the proposed method remains a ConvNeXt/U-shaped convolutional decoder and uses bounded residual guidance of MSCB branches at Stage 3.
- Low-to-moderate risk from general attention/gating modules. Avoid broad claims such as "first frequency-guided adaptive multi-scale segmentation block" unless a deeper systematic review confirms that claim.
- Any novelty claim should be limited to the three precise constraints supplied by the authors: FAFEM descriptor to MSCB branch weighting, bounded residual guidance, and bottleneck-to-Stage-3 cross-level guidance.

## 9. Proposed Subsection Structure

- Convolutional and transformer encoder-decoder segmentation.
- Efficient multi-scale convolutional decoding.
- Frequency-aware and adaptive feature recalibration.
- Recent polyp segmentation with boundary/frequency/context modeling.
- Positioning of the proposed residual frequency-guided coupling.
