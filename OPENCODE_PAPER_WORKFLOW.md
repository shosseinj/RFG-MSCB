# OpenCode + K-Dense workflow for the paper

## 1. Install

Open PowerShell in the root folder of your LaTeX paper project.

Extract this setup ZIP somewhere, then copy these files into the paper root or call them by full path.

Recommended installation:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\install_kdense_opencode.ps1
```

To install every K-Dense skill:

```powershell
.\install_kdense_opencode.ps1 -All
```

The installer keeps a clone under:

```text
.vendor/scientific-agent-skills/
```

and copies the selected skills into:

```text
.opencode/skills/
```

OpenCode discovers `.opencode/skills/<skill>/SKILL.md` automatically.

After installation, restart OpenCode from the paper project root.

## 2. Verify

```powershell
.\verify_opencode_skills.ps1
```

Inside OpenCode, ask:

```text
List the available skills relevant to scientific paper writing.
```

You can also explicitly instruct OpenCode to load a skill by name.

## 3. Recommended skills for this paper

- `scientific-writing`
  - academic prose, section revision, clarity, structure

- `research-lookup`
  - verify claims and find supporting references

- `literature-review`
  - rebuild/extend Related Work and identify research gaps

- `scientific-critical-thinking`
  - challenge novelty claims, interpretation, and evidence

- `peer-review`
  - final reviewer-style audit before submission

## 4. Safe paper-editing rule

Use this instruction at the start of major OpenCode sessions:

```text
This is a near-final scientific manuscript.

Before editing, inspect the relevant LaTeX section and any related Method,
results, tables, and references.

Do not invent citations, experimental results, architecture details,
dataset splits, parameter counts, or numerical values.

FAFEM and MSCB are reused prior modules and must not be presented as our inventions.

The paper's architectural novelty is the residual frequency-guided coupling:
a bottleneck FAFEM frequency descriptor adaptively controls the multi-scale
MSCB branches at Stage 3 using bounded residual guidance.

Make the smallest necessary edits.
Do not change unrelated sections.
When scientific evidence is missing, flag it instead of inventing it.
Build the LaTeX project after edits and report compilation warnings/errors.
```

## 5. Suggested workflow from the current stage

### A. Related Work

```text
Use the literature-review and research-lookup skills.

Audit sections/02_related_work.tex against the final Method.

Goals:
1. Remove discussion that only motivates removed modules.
2. Organize the section around:
   - polyp segmentation architectures,
   - frequency-aware feature modeling,
   - multi-scale convolution/adaptive scale processing.
3. Identify the original sources for FAFEM and MSCB/EMCAD.
4. Verify every new citation before adding it.
5. Clearly distinguish prior work from our RFG-MSCB contribution.

Do not invent bibliographic metadata.
First produce a proposed revision plan and citation audit.
Then edit the section.
```

### B. References

```text
Use research-lookup.

Audit references.bib and every \cite{...} used by the manuscript.

Verify titles, authors, venue, year, DOI/article number where available.
Merge duplicates.
Do not fabricate missing metadata.
Create REFERENCE_AUDIT.md for unresolved entries.
```

### C. Experiments

```text
Use scientific-writing and scientific-critical-thinking.

Audit sections/04_experiments.tex.

Treat implementation code, evaluation summaries, and experiment outputs as the
source of truth. Do not reuse stale settings from older model versions.

Check:
- datasets and splits,
- optimizer,
- learning rates,
- scheduler,
- epochs,
- batch size,
- loss,
- threshold,
- checkpoint selection,
- metrics,
- parameter count,
- hardware,
- TTA policy.

Flag any claim that is not supported by the final experiment artifacts.
```

### D. Ablation Study

```text
Use scientific-writing and scientific-critical-thinking.

Build the ablation narrative only from actual completed experiments.

The ablation must distinguish:
- baseline,
- FAFEM,
- MSCB-lite where available,
- frequency-guided MSCB,
- residual frequency-guided MSCB,
- placement variants where actually tested.

Do not claim that an ablation exists unless its result is present in the project.
For every claimed improvement, compute the exact delta from reported values.
```

### E. Discussion / Conclusion

```text
Use scientific-writing and scientific-critical-thinking.

Write Discussion based only on verified results.
Separate:
- observations,
- supported interpretation,
- limitations,
- future work.

Avoid generic statements such as "significantly improves" unless supported by
the reported evidence.

Then write a concise Conclusion consistent with the verified contributions.
```

### F. Final peer review

```text
Use peer-review.

Review the complete manuscript as a critical journal reviewer.

Check:
- novelty and ownership claims,
- internal consistency,
- reference correctness,
- unsupported claims,
- experiment fairness,
- data leakage/checkpoint-selection risks,
- table/figure numbering,
- equation numbering,
- undefined acronyms,
- cross-references,
- limitations,
- reproducibility.

Do not edit first.
Create FINAL_PEER_REVIEW.md with major and minor issues ranked by severity.
```

## 6. Recommended sequence

1. Related Work + reference verification
2. Experiments / implementation details
3. Quantitative comparison tables
4. Ablation Study
5. Discussion
6. Conclusion
7. Abstract
8. Final peer review
9. Final LaTeX formatting / journal template migration

Do the Abstract near the end because it must reflect the final verified results.
