# Project conventions for Claude

This repository is the index for the Swiss Public Data MCP servers.
`portfolio.json` is the source of truth; the READMEs, the registry manifests,
the install snippets and the promotion page are **generated** from it and held
to it by `readme-sync.yml` on every pull request. Never hand-edit anything
between `<!-- BEGIN GENERATED: … -->` markers — see `CONTRIBUTING.md` for the
edit-and-regenerate loop.

(No server count here on purpose: it would be a hand-copied number in a file
about not hand-copying numbers. `scripts/coverage_manifest.py --check` prints
the current one.)

## How verification works here

These rules exist because the failures below happened in this portfolio, all
within a few days, and all of them the same shape: **the check ran and checked
nothing.** They are not style. Each one produced a confident, false report.

### Check the result, not the activity

- Never test for a running process with `pgrep -f '<your own pattern>'`. The
  pattern is in the command line you are searching with, so `pgrep` finds
  itself. Test the result instead: `[ -s file ]`, `ls -l`, an exit code.
  *A sweep was reported as "still running" twice, two hours after it finished.*

- Never write `command; echo ok`. The semicolon separates, it does not connect.
  Use `command && echo ok`, or read the state afterwards — the remote ref, the
  file, the API.
  *A push was reported as done while `git` was saying `the remote end hung up
  unexpectedly`.*

- In a pipeline, `$?` is the **last** command's status. `cmd | head` reports
  `head`. Use `${PIPESTATUS[0]}` or drop the pipe.

### A pattern that claims absence must first be proven on a known positive

A grep too narrow finds nothing and looks like a clean result. So does a stub
that never matches.

*Three releases were reported missing because the grep pattern was too narrow.
And an exit-code harness reported failure for every case — including the ones
that pass — because `next(gen, default)` evaluates the default eagerly, so the
stub raised on every call. A working script was nearly "repaired".*

### Run the check that counts, not the one you know

Read what CI actually runs before claiming a local pass. `ruff check` and
`ruff format --check` are two commands; passing the first and reporting "ruff
clean" is a false statement about the second.

## The rule underneath all of it

Every report here distinguishes three answers, never two:

* **clean** — the check ran and found nothing,
* **finding** — the check ran and found something,
* **not measured** — the check did not run, or could not conclude.

"I did not look" and "there was nothing there" must not share an exit code, and
they must not share a sentence either. `scripts/coverage_manifest.py` exists
because a portfolio sweep once reported "33 of 33 ok" while `portfolio.json`
listed 43 servers — the sentence was true and the set was wrong, and nothing
contradicted it because nothing compared it against the source of truth.

The same rule applies to closing a finding: **an explanation that names no
measurement has not closed anything.** A confirmed circular import in
`bag-health-mcp` was dismissed as an import-order artefact, on reasoning rather
than a second measurement. The reasoning was wrong and the probe was right.

A finding without its observation is an opinion.
