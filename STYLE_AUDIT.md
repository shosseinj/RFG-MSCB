# Style Audit

## Recurring patterns

1. Explicit ownership disclaimers were repeated for FAFEM and MSCB, for example “FAFEM is prior work, not a contribution of this paper” and “MSCB is prior work and is not introduced in this paper.” The repetition makes the prose sound defensive.
2. Routine architecture descriptions repeatedly used “the proposed framework,” “the proposed model,” and “the proposed method,” even when describing fixed implementation details.
3. Several paragraphs used generic result conclusions such as “This configuration establishes the baseline,” “These results support...,” and “This demonstrates...,” rather than stating the measured comparison and its scope.
4. Some wording implied stronger evidence than the design supports, including broad generalization language and effectiveness-oriented phrasing for descriptive, small-seed differences.
5. Transitions such as “This observation motivates the central idea of this work” and “The central objective...” added framing without advancing the technical description.

## Representative rewrites

| Before | After | Rationale |
|---|---|---|
| “FAFEM is prior work, not a contribution of this paper.” | “We adopt FAFEM at the bottleneck to obtain the frequency descriptor used for decoder guidance.” | Keeps ownership clear through the verb “adopt” without a disclaimer. |
| “MSCB is prior work and is not introduced in this paper.” | “MSCB serves as the multi-scale reference path, with parallel branches providing different receptive fields.” | Identifies the reused role directly. |
| “The proposed framework follows a U-shaped...” | “The network uses a U-shaped...” | Removes unnecessary ownership language from a routine description. |
| “These results support bounded cross-level frequency guidance as a viable refinement strategy.” | “The ablation measures the effect of bounded cross-level frequency guidance under the tested protocol.” | Avoids promotion and limits the claim to the experiment. |
| “This demonstrates the effectiveness of...” | “The measured change was...” | Separates observation from interpretation. |
| “The proposed method did not attain...” | “The model did not attain...” | Uses a concrete subject and avoids repetitive phrasing. |

## Revision approach

The revised manuscript uses “we adopt” or “building on” for reused components, reserves “we introduce” for the RFG-MSCB coupling and bounded guidance formulation, and reports result directions without claims of significance, superiority, or robust generalization that are not established by the experiments. Numerical values, equations, citations, and architecture meaning were retained.
