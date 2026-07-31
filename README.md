# Signed Faithfulness for Luce Choice Events

This repository contains a short probability paper about top-choice events extracted from one
Plackett--Luce ranking.

For independent exponential clocks $X_v\sim\operatorname{Exp}(\lambda_v)$, define

\[
C(S,s)=\{X_s<X_v\text{ for every }v\in S\setminus\{s\}\}.
\]

The paper gives the exact covariance of any two such events. Its sign depends only on how the two
menus and their nominated winners overlap:

| Geometry | Covariance sign |
|---|---:|
| Same nominated winner | Positive |
| Shared competitors, neither winner crosses menus | Positive |
| One winner belongs to the other menu | Negative, except for one nested zero case |
| Each winner belongs to the other menu | Negative |
| Disjoint menus | Zero |
| Properly nested menus, with the larger-menu winner outside the smaller menu | Zero |

The zero cases form pivot-labelled laminar forests. This yields two further conclusions:

- every pairwise-independent finite family is mutually independent;
- a family with $r$ maximal menus on $n$ used items has at most $n-r$ events, with equality
  exactly for disjoint unions of full flags.

The statements also hold for independent clocks with a common proportional-hazards baseline.

## Repository map

- [`signed_faithfulness_luce_choices.tex`](signed_faithfulness_luce_choices.tex): manuscript source
- [`novelty_and_submission_notes.md`](novelty_and_submission_notes.md): closest results, exact novelty
  boundary, and remaining review risks
- [`verification/exact_verification.py`](verification/exact_verification.py): exhaustive rational checks
  on finite Plackett--Luce rankings
- [`submission/arxiv_metadata.md`](submission/arxiv_metadata.md): provisional preprint metadata
- [`FUTURE_VERIFICATION_GATE.sh`](FUTURE_VERIFICATION_GATE.sh): clean-checkout verification and build
  gate

## Verification

The exact verifier reconstructs the Plackett--Luce law by summing over every permutation. It compares
those probabilities with each covariance formula, enumerates pairwise-independent cliques for four
items, checks their full joint factorization, and checks the extremal bound.

Under normal compute resources:

```sh
./FUTURE_VERIFICATION_GATE.sh --verify
```

The verifier and LaTeX build remain unexecuted during the resource-constrained drafting window, so
no compiled PDF is included yet.

## Research status

The Plackett--Luce race representation, record-chain independence, and ranking decomposability are
classical. The proposed contribution is the combined exact covariance, structural zero-set,
pairwise-to-mutual collapse, and extremal classification. No exact prior formulation was found in
the documented web-indexed search. Independent proof review and searches in MathSciNet, zbMATH,
Scopus, and Web of Science remain necessary before submission.
