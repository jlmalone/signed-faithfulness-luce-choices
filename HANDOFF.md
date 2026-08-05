# Project handoff

Updated 5 August 2026.

## Outcome

The repository contains a complete short research-note candidate on dependence among top-choice
events extracted from one Plackett--Luce ranking. The public repository is:

<https://github.com/jlmalone/signed-faithfulness-luce-choices>

The canonical branch is `master`. The manuscript proofs are the mathematical source of truth.

## Core result

For independent exponential clocks, the manuscript proves:

1. an exact covariance formula for every pair of specified-winner menu events;
2. a covariance sign determined entirely by menu and pivot geometry;
3. zero covariance exactly for disjoint menus or oriented nested menus;
4. equivalence of pairwise independence, mutual independence, and pivot-laminarity for every finite
   family;
5. the sharp bound $m\le n-r$, with equality exactly for disjoint unions of full flags;
6. the same conclusions for independent races with a common proportional-hazards baseline.

The result concerns several choice features derived from one latent ranking. Choices generated from
fresh independent rankings form a different experiment.

## Repository contents

- `signed_faithfulness_luce_choices.tex` contains the definitions, theorems, proofs, limitations,
  and bibliography.
- `verification/exact_verification.py` reconstructs finite Plackett--Luce laws by exact rational
  summation over permutations. It checks every covariance case, the structural zero-set, finite
  joint factorization, and the extremal bound.
- `novelty_and_submission_notes.md` records the exact novelty claim, closest checked work, search
  vocabulary, and remaining novelty risks.
- `submission/arxiv_metadata.md` contains provisional preprint metadata.
- `FUTURE_VERIFICATION_GATE.sh` runs the exact verifier and builds the manuscript from a clean
  checkout.

## Established state

- The public GitHub repository exists and uses `master` as its default branch.
- The manuscript contains self-contained proofs of the covariance, independence-collapse, extremal,
  and proportional-hazards results.
- The classical ingredients and the proposed contribution are separated explicitly.
- The novelty claim is limited to the combined signed-dependence and laminar-family package.
- The tracked material contains no operator-specific paths or private review material.
- Static repository checks and LaTeX environment-balance checks are clean.

## Unverified gates

The following claims have not been established:

- The exact verifier has not been executed during the resource-constrained drafting window.
- The LaTeX source has not been compiled or visually inspected as a rendered PDF.
- No independent probability researcher has audited the proof.
- No ranking-model specialist has checked whether the result is implicit in the full
  L-decomposability, split-and-splice, rank-breaking, or composite-likelihood literature.
- MathSciNet, zbMATH, Scopus, and Web of Science have not been searched exhaustively.
- Novelty, publishability, journal acceptance, and arXiv eligibility are not certified.

## Owner decisions still needed

These choices should not be inferred automatically:

1. repository and manuscript license;
2. final author list, affiliation, and contact details;
3. arXiv license and final subject classification;
4. first venue or preprint route;
5. whether a public compiled PDF belongs in the repository;
6. whether to use the term “faithfulness” in the final title after specialist review.

Public visibility alone does not grant a reuse license. Add one only after the intended permissions
are chosen.

## Recommended path to version 0.1

1. Run the future gate from a clean checkout:

   ```sh
   ./FUTURE_VERIFICATION_GATE.sh --verify
   ```

2. Inspect every rendered page, with particular attention to equation breaks, theorem numbering,
   bibliography links, and title-page spacing.
3. Repair any verifier, compilation, or rendering defect without weakening the theorem hypotheses.
4. Obtain an independent line-by-line proof audit.
5. Complete the closed-index novelty search described in `novelty_and_submission_notes.md`.
6. Revise the contribution statement to reflect any newly found precursor.
7. Fill the author and license fields, then choose the first specialist venue or preprint route.
8. Tag a reviewed version and attach the inspected PDF only after the preceding gates pass.

Version 0.1 is complete when the exact gate passes, the PDF is visually clean, the novelty ledger is
current, the proof has independent scrutiny, and the legal and submission metadata are explicit.

## Publication positioning

Keep the first paper concise. Its strongest contribution is the unified structural theorem:
parameter-free covariance signs, an exact independence zero-set, pairwise-to-mutual collapse, and a
sharp extremal classification. The exponential race representation, record-chain independence,
memorylessness, and proportional-hazards transformation are classical ingredients.

A specialist short-note venue is the natural scale. Avoid expanding the manuscript with generic
applications. Any application must genuinely use overlapping choices from the same latent ranking.
Repeated independent choice occasions would remove the dependence problem.

## Refinement if the current note is judged too small

Pursue one mathematically consequential extension rather than several routine corollaries. The most
promising directions are:

1. characterize dependence for top-$k$, winner-in-subset, or partial-ranking events;
2. determine conditional-independence relations among overlapping menu features;
3. use the covariance formulas in a rank-breaking or composite-likelihood variance calculation;
4. characterize common proportional hazards through nested choice-event independence;
5. extend the structural classification to countable races under explicit summability conditions.

Each direction needs its own counterexample search and literature audit before entering the paper.
The current theorem should remain intact as a short note if none of these extensions produces a
substantial result.

## Do not break

- Keep all rates strictly positive and all menus non-singleton.
- Preserve the distinction between a shared latent ranking and fresh independent rankings.
- Do not describe finite enumeration as proof of the general theorem.
- Do not claim that a negative literature search certifies novelty.
- Do not select a license, submission agreement, or author metadata without an explicit decision.
- Keep private correspondence, reviewer identities, and submission credentials out of the public
  repository.
