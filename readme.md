# RFG-MSCB: Frequency-Guided Multi-Scale Refinement for Polyp Segmentation

This repository contains an ongoing research project on colorectal polyp segmentation using a ConvNeXt-Tiny encoder and a U-shaped decoder. The main focus is on using information extracted from low- and high-frequency components at the bottleneck to guide multi-scale feature refinement in the decoder.

## Method Overview

The framework combines three main components:

- **ConvNeXt-Tiny encoder** with four hierarchical stages.
- **Frequency-Aware Feature Enhancement Module (FAFEM)** at the bottleneck, where low- and high-frequency components are processed separately and summarized into a compact frequency descriptor.
- **Residual Frequency-Guided Multi-Scale Convolution Block (RFG-MSCB)** at the Stage-3 encoder-decoder fusion, where the bottleneck descriptor modulates parallel depthwise branches with different receptive fields.

FAFEM and the underlying MSCB operations are adopted prior components rather than claimed inventions. MSCB is associated with the published EMCAD architecture; the contribution investigated here is the bounded residual, cross-level coupling that uses the bottleneck frequency descriptor to modulate Stage-3 MSCB branches. The exact scholarly source for the adopted FAFEM remains unresolved in the repository audit and should not be inferred from the project name.

For a 352 × 352 input, the encoder produces feature maps with channel dimensions `[96, 192, 384, 768]`. The frequency descriptor generated at the bottleneck is 1536-dimensional and is used to adapt the relative contribution of 1 × 1, 3 × 3, and 5 × 5 depthwise branches.

## Research Motivation

Polyp appearance varies substantially in size, contrast, texture, and boundary definition. The project investigates whether deep frequency information can provide useful global guidance for selecting receptive fields during decoder refinement, while retaining a stable residual path to the ordinary multi-scale convolution response.

## Experimental Protocol

The current study uses five public polyp-segmentation datasets and evaluates model variants across multiple random seeds. The experimental design includes controlled ablations from the baseline model through frequency enhancement and multi-scale refinement to the complete residual frequency-guided formulation.

The manuscript currently reports a five-dataset, three-seed mean mDice of **0.872** for the complete model, together with improvements across the positive-valued evaluation metrics considered in the study. These values should be interpreted as results from the current experimental version of the project rather than as a finalized publication claim.

## Repository Contents

- `manuscript.tex` — main LaTeX manuscript
- `sections/` — manuscript sections
- `media/` — architecture and qualitative figures
- `references.bib` — bibliography
- experimental and manuscript-support material used during the study

The implementation associated with the segmentation experiments is maintained in the related [Convnext-unet](https://github.com/shosseinj/Convnext-unet) repository.

## Building the Manuscript

The manuscript can be compiled with a standard LaTeX environment, for example:

```bash
xelatex manuscript.tex
bibtex manuscript
xelatex manuscript.tex
xelatex manuscript.tex
```

## Research Status

This repository documents work in progress. Experimental values, tables, and manuscript text may be revised as additional validation and ablation studies are completed.


## Goal

This repository is the evidence and manuscript workspace for defining RFG-MSCB precisely, checking its provenance, and reporting the associated polyp-segmentation experiments without mixing current results with archival drafts.

## Installation

No Python environment is required to read the evidence package. To build the paper, install a LaTeX distribution that provides XeLaTeX and BibTeX, then run the commands in the building section from the repository root.

## Working with the Repository

Edit the paper through `manuscript.tex`, `sections/`, and `references.bib`. Treat files whose names contain `AUDIT` and the material under `paper_evidence*/` as traceability records: numerical changes should be checked against those files before manuscript tables or claims are updated. Model development and inference belong in the linked `Convnext-unet` repository.
