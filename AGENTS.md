# Repository instructions

This repository contains one probability research note and its verification material.

## Sources of truth

- `signed_faithfulness_luce_choices.tex` contains the theorem statements and proofs.
- `HANDOFF.md` contains current state, unresolved gates, and the ordered path to a reviewed release.
- `novelty_and_submission_notes.md` records the bounded novelty claim and review risks.
- `verification/exact_verification.py` checks finite instances with exact rational arithmetic.
- `submission/arxiv_metadata.md` contains provisional submission metadata.

Keep mathematical claims synchronized across these files. The proofs remain authoritative; finite
enumeration is a transcription and counterexample check.

## Workflow

- `master` is the canonical branch.
- Keep generated LaTeX artifacts out of version control except for a deliberately reviewed PDF.
- Preserve strict positivity and non-singleton menu hypotheses in every theorem statement.
- Describe the model as choices extracted from one latent ranking. Fresh independent rankings are a
  different experiment.
- Treat novelty and publication status as provisional until independent expert and closed-index
  review are complete.
- Under normal resources, run `./FUTURE_VERIFICATION_GATE.sh --verify` before committing a manuscript
  revision.
