# Pre-edit diagnosis and revision plan

Review date: 2026-09-05. Author-requested pre-submission assessment, not an assigned journal review or editorial decision. Human author verification remains required. Target journal is not identified. Original source and PDF are preserved in `before/`. Public titles/identifiers alone are used for external literature checks; manuscript text is processed within the authorized workspace.

## Stage 1: manuscript map

The study asks whether a deep low/high spatial-frequency proxy can condition multi-kernel decoder refinement in a ConvNeXt-Tiny U-shaped polyp segmenter. It uses bottleneck FAFEM, a 1536-dimensional descriptor, and three Stage-3 MSCB branches combined by a bounded residual gate. The intended evidence is five public datasets and component ablation. The manuscript claims a 1305/145 development split plus independent 100/62 seen tests, three seeds, and 30.06 M parameters. Current tables claim higher overlap scores on several datasets; the abstract instead highlights an ablation with different Kvasir scores.

Read all active TeX sections, front matter, references, and the relevant dataset/configuration/evaluation/architecture/ablation packages. Historical audits were used as leads, not presumed current findings. Current source snapshots and raw evaluation JSON were inspected. No experiments were rerun. Scope covers technical and reporting appraisal; it cannot certify clinical safety, ethics, or novelty exhaustively.

## Stage 2: diagnostic findings

| ID | Severity | Location | Finding and consequence |
|---|---|---|---|
| C1 | CRITICAL | Dataset and selection sections; abstract; discussion; conclusion | Claimed independent tests conflict with source snapshots: 900+550 train and 100+62 merged checkpoint-validation images. Current scores also differ from bundled evaluation JSON. New runs may exist, but their provenance is absent here. Old results cannot establish independent seen-test performance. |
| C2 | CRITICAL | Kvasir and ColonDB comparison tables | Ours has mean E > maximum E (0.972 > 0.968; 0.919 > 0.911). Impossible for the same E-curve and averaging population. This is a demonstrable numerical inconsistency, not evidence of misconduct. |
| C3 | CRITICAL | Ablation table and abstract | Final Kvasir mDice/mIoU 0.875/0.815 conflicts with main 0.932/0.883 and archived 0.931284/0.882594. No row-to-run provenance; archived bare baseline has a different optimization protocol. Component attribution is unsupported until reconciled. |
| M1 | MAJOR | Comparative study | Published table entries largely lack primary table/page support. Matched image counts do not establish identical image identities, checkpoint selection, evaluation resolution, or metric definitions. Several rank decorations are wrong. |
| M2 | MAJOR | Related work and novelty | Frequency-polyp precedents FAENet, M3FPolypSegNet, PSTNet, and recent cross-scale frequency fusion need consideration. SE/SK/FcaNet alone do not adequately establish the polyp-specific gap. |
| M3 | MAJOR | Data handling and generalization | No patient/video grouping or overlap manifest; external checkpoint exclusion does not prove absence of test-guided architecture/threshold selection. Clinical utility is not established by retrospective image metrics. |
| M4 | MAJOR | Methods/evaluation | Unclear metric resolution versus original resolution, uncertain metric-package normalization/version, reused P for logits and binary prediction, ambiguous boundary-loss reductions. |
| M5 | MAJOR | Front matter/declarations | Empty author field; no affiliations/keywords/funding/contributions/ethics explanation/AI statement; competing-interest statement requires author confirmation. Journal-specific requirements unknown. |
| M6 | MODERATE | Methods | DropPath is linearly scheduled from 0 to 0.25, not constant throughout. Projection definition appears to include shuffle twice. “Bounded” applies to gate/branch coefficients, not feature norm or optimization stability. |
| M7 | MODERATE | Section organization | Ablation is a top-level section nested inside Experiments; subsequent comparative study inherits the wrong parent. No active figures. |
| M8 | MINOR | Results prose and bibliography | External ranges use stale minima; FcaNet pages differ from the primary CVF record. Other metadata require identifier-level audit. |

## Stage 3: prioritized revision plan

1. Preserve all tables verbatim and report their defects; add visible author-query warnings near unresolved evidence. Do not replace them with old-protocol values.
2. Bound abstract, contributions, comparison, discussion, and conclusion to available evidence. Treat new split as intended pending run provenance, not a completed verified experiment.
3. Correct source-grounded notation, DropPath description, loss reduction, hierarchy, and numerical-range prose. Clarify limits of the frequency proxy and residual gate.
4. Verify public literature and bibliography; add narrowly relevant supported context without copying competitor superiority claims.
5. Consolidate author queries, journal checks, section reviews, and a simulated verdict in the final report.
6. Recompute local artifact summaries; audit labels/citations/table preservation, build LaTeX, inspect the PDF, and perform a skeptical second pass. Record unresolved defects honestly.

## Skill application

Applied scientific-writing evidence binding and missing-information rules, peer-review location/problem/action structure, critical-thinking checks for confounding and generalization, literature-review scoping and claim-source synthesis, and research-lookup primary-source verification. This is a targeted literature audit, not a systematic review; no PRISMA completeness claim or automatic figure generation is appropriate. The Parallel CLI is absent; built-in web and public Crossref retrieval provide the requested capabilities without installing software. Paper-lookup supplies identifier validation and provenance discipline; PDF skill supplies local rendering checks. Journal-assigned-review intake requirements are not represented as satisfied: this is expressly author-authorized manuscript preparation, and journal policy remains pending.
