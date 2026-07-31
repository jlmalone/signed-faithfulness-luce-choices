#!/bin/sh
set -eu

repo_name=signed_faithfulness_luce_choices
repo_root=$(CDPATH= cd "$(dirname "$0")" && pwd -P)

die() {
    printf '%s\n' "verification gate: $*" >&2
    exit 1
}

usage() {
    printf '%s\n' "usage: ./FUTURE_VERIFICATION_GATE.sh --verify"
}

[ "$#" -eq 1 ] || { usage; exit 1; }
[ "$1" = "--verify" ] || { usage; exit 1; }
[ "$(basename "$repo_root")" = "$repo_name" ] || die "expected repository basename $repo_name"

git_root=$(git -C "$repo_root" rev-parse --show-toplevel 2>/dev/null) || die "not a Git worktree"
[ "$git_root" = "$repo_root" ] || die "script must remain at the Git worktree root"
[ -z "$(git -C "$repo_root" status --porcelain)" ] || die "a clean checkout is required"

git -C "$repo_root" diff --check
[ -f "$repo_root/signed_faithfulness_luce_choices.tex" ] || die "manuscript source is missing"
[ -f "$repo_root/verification/exact_verification.py" ] || die "exact verifier is missing"

command -v python3 >/dev/null 2>&1 || die "Python 3 is required"
python3 "$repo_root/verification/exact_verification.py"

cd "$repo_root"
if command -v tectonic >/dev/null 2>&1; then
    tectonic signed_faithfulness_luce_choices.tex
elif command -v pdflatex >/dev/null 2>&1; then
    pdflatex -halt-on-error -interaction=nonstopmode signed_faithfulness_luce_choices.tex
    pdflatex -halt-on-error -interaction=nonstopmode signed_faithfulness_luce_choices.tex
else
    die "Tectonic or pdflatex is required"
fi

[ -f "$repo_root/signed_faithfulness_luce_choices.pdf" ] || die "PDF build did not produce output"
printf '%s\n' "Exact finite verification and LaTeX compilation completed. The manuscript proofs remain authoritative."
