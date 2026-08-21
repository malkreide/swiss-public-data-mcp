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

The same trap in documents: a check can answer a narrower question than the
one you needed and still come back green.

*A sweep verified that every `CLAUDE.md` carried the shared conventions in
full, and concluded from that the files were correct. The check could not see
part two — the repo-specific half — which the same sweep had just made wrong.
Thirteen files went on telling contributors to install a pinned tool by hand
after the pin had moved. A reviewer found it, not the sweep.*

### Copies that agree still prove nothing if one of them overrides the rest

A guard that compares N places and demands they match reports "clean" the
moment they match. That says nothing about whether the match matters.

*The ruff version was pinned in `pyproject.toml` and again as an install step
in CI. The numbers agreed, and a guard checked that they agreed. But the CI
step ran **after** the dependency install and overwrote it, so a loosened
range in `pyproject.toml` could never turn CI red — it would only have hurt
locally, where nobody expects it. The guard was green throughout.*

Where a place must not exist, check for its **absence**, separately, and
independently of its value. Equality between the survivors is the weaker
claim, and a returning copy satisfies it while defeating it.

## The ruff pin: one source per repository

In the servers the pin lives in `pyproject.toml`, `dev` extra, `ruff==X.Y.Z`,
and **no workflow installs ruff itself**. Where a `.pre-commit-config.yaml`
exists it repeats the number, because pre-commit cannot read `pyproject.toml`;
those two must agree, and a guard says so.

**This repository is the exception, and deliberately so.** It has no
`pyproject.toml` — it is the portfolio bracket, not a Python package — so the
pin lives in `.github/workflows/lint.yml` and only there. That is still one
source. Do not "align" it with the servers by inventing a package here.

Two traps, both hit during the portfolio-wide consolidation:

- A job whose **only** ruff came from the pin step. Deleting the step without
  putting an install in its place leaves `ruff: command not found`, exit 127.
  Seven servers had such a `lint` job. The replacement install is not a
  duplicate of the one in the test job, and a comment should say so — it looks
  exactly like something to tidy away.
- Drift guards that encoded the old shape. Four of them went red on the
  change, which is what guards are for. They were rewritten to the stronger
  invariant, not deleted.

## This repository's gates

Eight checks run on a pull request, across two workflows. None of them is a
test suite: there is no `src/`, no `pyproject.toml` and no server here.

`lint.yml` — note the scope is `scripts/` alone (10 files), not the
`src/ tests/ scripts/` the servers lint:

```bash
ruff check scripts/
ruff format --check scripts/
```

`readme-sync.yml`:

```bash
python -c "import json; json.load(open('portfolio.json'))"
python scripts/coverage_manifest.py --check
python scripts/generate_readme.py --check
python scripts/generate_server_json.py --check
python scripts/generate_install_snippets.py --check
```

The three `generate_*.py --check` gates print **nothing** and exit 0 when they
pass. Silence is the success signal here, so an empty log is not evidence the
step was skipped — read the exit code, not the output. Only
`coverage_manifest.py --check` says anything (`repositories OK (47; …)`).

A third workflow, `index-presence.yml`, runs on a schedule
(`cron: "37 4 * * *"`) and asks the package index whether every `pypi_dist`
in `portfolio.json` really exists. It is this repo's equivalent of the
servers' live tests — the only check whose input is somebody else's system,
and therefore the only one a green pull request cannot speak for.

## Before you open a PR

Read `main`, not just your clone. Of thirty-three pull requests in one
portfolio pass, four were duplicates: parallel sessions had already landed the
same change, in two cases with a guard the newer branch lacked. The conflict
only surfaces at merge time, and then the question is whose version wins —
often the other one.

Before creating a branch whose name was handed to you, ask whether it already
exists:

```bash
git ls-remote --heads origin claude/<name> | wc -l
```

`1` means somebody else is on it, with write access to the same ref.

**A pull request with an empty diff gets closed, not merged.** The test is
`get_files` on the pull request: `[]` means it changes nothing. A green check
is no evidence against that — CI runs the head, and the head is fine; what is
empty is the difference to the base.

*In a later pass two sessions ran the same task across forty-five
repositories, on two branches. Wherever one reached `main` first, `main` was
merged into the other's branch and the add/add conflict resolved in favour of
`main`. Fourteen pull requests came out of that: green through every gate, and
carrying nothing. They were merged and left empty merge commits. With the two
follow-ups that were moot for the same reason, sixteen of that day's
fifty-nine pull requests were pure friction.*

Same shape as everything under *How verification works here*: the check ran and
checked nothing.

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
