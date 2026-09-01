# Equation Audit

## Scope

Audited `manuscript.tex` and every file under `sections/`, with detailed review of the Method, Experiments, and Ablation Study. The audit distinguishes scientific operations that need stable equation numbers from dimensions, constants, table symbols, and repeated derivations that should not consume equation numbers.

## Classification Summary

| Classification | Decision |
|---|---|
| SHOULD BE NUMBERED | Core encoder, bottleneck, FAFEM, MSCB, guidance, decoder, prediction, loss, and overlap-metric operations listed below |
| SHOULD REMAIN UNNUMBERED | Tensor dimensions, normalization constants, architecture lists, kernel sets, initialization identities, scalar bounds, and parameter counts |
| INLINE EQUATION | Input domain, fixed channel/depth lists, descriptor size, concrete dimensions, prediction-head channel progression, and symbols used in table headers |
| DUPLICATE / REDUNDANT | Introductory RFG formula and repeated progressive-decoder equations; replaced with references to the definitive Method equations |

All legacy `$$...$$` displays were removed. Numbered derivations now use `equation` or `align`; retained unnumbered displays use `\[...\]`.

## Numbered Equations

### Overall Architecture and Encoder

| Operation | Label | Classification |
|---|---|---|
| Hierarchical encoder feature extraction | `eq:encoder_features` | SHOULD BE NUMBERED |
| FAFEM output in architecture summary | `eq:overall_fafem` | SHOULD BE NUMBERED |
| Lightweight bottleneck in architecture summary | `eq:overall_bottleneck` | SHOULD BE NUMBERED |
| Stage-3 RFG decoder operation | `eq:overall_stage3` | SHOULD BE NUMBERED |
| Subsequent decoder stages | `eq:decoder_stage2`, `eq:decoder_stage1`, `eq:decoder_final` | SHOULD BE NUMBERED |
| ConvNeXt depthwise/pointwise transform | `eq:convnext_transform` | SHOULD BE NUMBERED |
| ConvNeXt residual output | `eq:convnext_residual` | SHOULD BE NUMBERED |

### FAFEM and Bottleneck

| Operation | Label | Classification |
|---|---|---|
| Low-frequency approximation | `eq:fafem_low_frequency` | SHOULD BE NUMBERED |
| High-frequency residual | `eq:fafem_high_frequency` | SHOULD BE NUMBERED |
| Low-/high-frequency branch transforms | `eq:fafem_frequency_transforms` | SHOULD BE NUMBERED |
| Globally pooled frequency descriptor | `eq:frequency_descriptor` | SHOULD BE NUMBERED |
| Residual FAFEM output | `eq:fafem_residual_output` | SHOULD BE NUMBERED |
| Bottleneck channel reduction | `eq:bottleneck_reduction` | SHOULD BE NUMBERED |
| Lightweight residual bottleneck | `eq:lightweight_bottleneck` | SHOULD BE NUMBERED |

### MSCB and Residual Frequency Guidance

| Operation | Label | Classification |
|---|---|---|
| MSCB channel expansion | `eq:mscb_expansion` | SHOULD BE NUMBERED |
| Multi-scale branch response | `eq:mscb_branches` | SHOULD BE NUMBERED |
| Ordinary MSCB aggregation | `eq:mscb_ordinary_aggregation` | SHOULD BE NUMBERED |
| Frequency-guidance logits | `eq:rfg_logits` | SHOULD BE NUMBERED |
| Normalized branch weights | `eq:rfg_weights` | SHOULD BE NUMBERED |
| Frequency-guided aggregation | `eq:rfg_guided_aggregation` | SHOULD BE NUMBERED |
| Bounded residual RFG formulation | `eq:rfg_residual` | SHOULD BE NUMBERED |
| Final Stage-3 residual output | `eq:rfg_final_output` | SHOULD BE NUMBERED |

### Prediction and Experiments

| Operation | Label | Classification |
|---|---|---|
| Prediction logits | `eq:prediction_logits` | SHOULD BE NUMBERED |
| Prediction resize | `eq:prediction_resize` | SHOULD BE NUMBERED |
| Foreground probability | `eq:prediction_probability` | SHOULD BE NUMBERED |
| Composite training objective | `eq:loss` | SHOULD BE NUMBERED |
| Per-image Dice and IoU | `eq:dice_iou` | SHOULD BE NUMBERED |

## Intentionally Unnumbered Displays

The following displays remain unnumbered because they document fixed values or supporting constraints rather than reusable operations:

- encoder feature tensor dimensions;
- ImageNet normalization mean and standard deviation;
- Stage-3 tensor dimensions at generic and 352-by-352 resolutions;
- guidance-network layer dimensions;
- normalized-weight sum and guidance-strength bound;
- equal initial branch weights and initial equality of guided and ordinary aggregation;
- concrete decoder tensor dimensions;
- exact and rounded parameter counts.

The input tensor domain, ConvNeXt stage depths/channels, bottleneck descriptor size, concrete tensor shapes, MSCB kernel set, prediction-head channel progression, guidance-network dimensions, scalar bounds, and initialization identities are inline. The metric symbols displayed inside comparison-table headers are formatting constructs, not equations, and are intentionally not numbered.

## Duplicate or Redundant Displays

- The Introduction previously repeated the bounded residual RFG equation. It now cites Eq.~`\eqref{eq:rfg_residual}` in the Method.
- The progressive decoder equations were previously repeated later in the Method. The later subsection now cites Eqs.~`\eqref{eq:decoder_stage2}`--`\eqref{eq:decoder_final}`.
- The approximate parameter count remains prose-supported and unnumbered rather than duplicating the exact count as a numbered equation.

## Reference and Label Checks

- Semantic equation labels added: 29.
- Duplicate equation labels: none.
- Undefined equation references: none after the two-pass build.
- Hard-coded equation numbers: none.
- Equation references use `Eq.~\eqref{...}` or `Eqs.~\eqref{...}`.
- Numbering is generated sequentially by LaTeX across the manuscript.
- Mathematical meaning was retained; only display environments, grouping, labels, references, and one notation typo (`\mathbf{z}_f`, `\mathcal{M}_{\mathrm{RFG}}`) were standardized.

## Build Result

Two-pass `pdflatex` compilation completed successfully and generated a 24-page `manuscript.pdf`. No undefined equation references, duplicate-label warnings, or LaTeX equation errors remain.

Remaining warnings are unrelated to equation numbering: small overfull `Epoch` headers, missing bold Greek glyphs in comparison-table headers, longtable infinite-glue warnings, an underfull Discussion line, overfull bibliography/image boxes, an empty-link warning near the ablation cross-reference, and the MiKTeX update notice.
