# Operator Runbook — publishing the portfolio to the MCP Registry

This is the step-by-step guide for taking the portfolio's servers live on the
official [MCP Registry](https://registry.modelcontextprotocol.io). It covers
one-time setup, the publishing pipeline, and the routine maintenance scripts.

`portfolio.json` is the single source of truth; everything else is generated or
derived from it. See [`registry/README.md`](registry/README.md) for the schema
and conventions behind the registry entries.

## Two kinds of scripts

| Script | Run where | When |
|---|---|---|
| `scripts/generate_readme.py` | **in this repo** | only when you edit `portfolio.json` |
| `scripts/generate_server_json.py` | **in this repo** | only when you edit `portfolio.json` |
| `scripts/patch_mcp_name.py` | **against the server repos** | publishing, step 1 |
| `scripts/release_all.py` | **against the server repos** | publishing, step 2 |
| `scripts/publish_registry.py` | **against the server repos** | publishing, step 3 |

The first two are *maintenance* (CI checks they stay in sync with
`portfolio.json`). The last three are the *publishing pipeline*.

Commands are given for **Windows PowerShell** and **macOS/Linux**. On Windows use
`python`; on macOS/Linux use `python3`.

---

## 0. One-time setup

### Directory layout

Keep this repo and a folder for the server repos side by side. **All scripts are
run from inside this repo.**

```
~/code/
├── swiss-public-data-mcp/   <- working directory; the scripts live in scripts/
└── repos/                   <- the server repos (populated by --clone)
```

PowerShell:
```powershell
mkdir ~\code; cd ~\code
git clone https://github.com/malkreide/swiss-public-data-mcp.git
mkdir repos
cd swiss-public-data-mcp
```

macOS/Linux:
```bash
mkdir -p ~/code && cd ~/code
git clone https://github.com/malkreide/swiss-public-data-mcp.git
mkdir -p repos
cd swiss-public-data-mcp
```

### Python build tooling (for `release_all.py`)

```bash
python -m pip install --upgrade build twine      # Windows
python3 -m pip install --upgrade build twine     # macOS/Linux
```

### Install the `mcp-publisher` CLI (for `publish_registry.py`)

**Windows (PowerShell):**
```powershell
$arch = if ([System.Runtime.InteropServices.RuntimeInformation]::ProcessArchitecture -eq "Arm64") { "arm64" } else { "amd64" }
Invoke-WebRequest -Uri "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_windows_$arch.tar.gz" -OutFile "mcp-publisher.tar.gz"
tar xf mcp-publisher.tar.gz mcp-publisher.exe
Remove-Item mcp-publisher.tar.gz

# Put it on PATH (publish_registry.py calls the bare name `mcp-publisher`)
New-Item -ItemType Directory -Force "$env:USERPROFILE\bin" | Out-Null
Move-Item -Force .\mcp-publisher.exe "$env:USERPROFILE\bin\"
$env:Path = "$env:USERPROFILE\bin;$env:Path"               # current session
setx PATH "$env:USERPROFILE\bin;$env:Path"                 # permanent (reopen the terminal)
```

**macOS/Linux:**
```bash
curl -L "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher && sudo mv mcp-publisher /usr/local/bin/
# or: brew install mcp-publisher
```

Verify: `mcp-publisher --help`.

> If you only ever call it by hand you can use `.\mcp-publisher.exe …` from the
> download folder, but `publish_registry.py` looks up the bare name on PATH —
> so for the pipeline it must be on PATH as shown above.

### Authenticate

```bash
mcp-publisher login github     # GitHub device flow; validates the io.github.malkreide namespace
```

PyPI credentials for `twine upload` (step 2):

PowerShell:
```powershell
$env:TWINE_USERNAME = "__token__"
$env:TWINE_PASSWORD = "pypi-XXXXXXXX"     # your PyPI API token
```
macOS/Linux:
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-XXXXXXXX
```
(Or store the token in `~/.pypirc`.)

---

## The publishing pipeline

Run everything from `~/code/swiss-public-data-mcp`. **Run each step as a dry run
first, then for real.** The order is mandatory — step 3 reads the PyPI metadata
produced by step 2.

### Step 1 — add the `mcp-name` marker to every README

For PyPI, the ownership marker is a line in the **README** (the package's long
description), written as an HTML comment — *not* a `[project.urls]` entry (PyPI
rejects non-URL values there):

```markdown
<!-- mcp-name: io.github.malkreide/<server-id> -->
```

```bash
# dry run: shows the plan only
python scripts/patch_mcp_name.py --repos-dir ../repos --clone

# live: edits README (and removes any old [project.urls] mcp-name), commits, pushes
python scripts/patch_mcp_name.py --repos-dir ../repos --clone --write --commit --push
```
`--clone` clones missing repos into `../repos` (and `git pull`s existing ones).

### Step 2 — cut a release per package (so `mcp-name` reaches PyPI)

```bash
# dry run: versioning mode + "current -> next" per repo
python scripts/release_all.py --repos-dir ../repos

# build + verify locally, no upload (recommended intermediate check)
python scripts/release_all.py --repos-dir ../repos --build

# live: bump/tag, build, verify mcp-name in the wheel, upload to PyPI
python scripts/release_all.py --repos-dir ../repos --commit --push --upload
```
Only uploads packages whose built wheel actually carries the `mcp-name` marker.
Needs the PyPI token.

### Step 3 — publish to the registry

```bash
# dry run: readiness report (READY / NOT_ON_PYPI / MISSING_MCP_NAME)
python scripts/publish_registry.py --repos-dir ../repos --clone

# live: publishes every server reported READY
python scripts/publish_registry.py --repos-dir ../repos --clone --publish
```
Needs an active `mcp-publisher login github` session.

### Verify

```bash
curl "https://registry.modelcontextprotocol.io/v0/servers?search=io.github.malkreide"
```

---

## Maintenance scripts (only when `portfolio.json` changes)

When you add/rename a server or edit descriptions, regenerate the derived files
**in this repo** and commit them, or CI will fail:

```bash
python scripts/generate_readme.py        # updates README.md / README.de.md
python scripts/generate_server_json.py   # updates registry/*/server.json
git add -A; git commit -m "…"; git push
```

CI runs both with `--check`. Adding a credential server? Set both
`requires_credentials: true` **and** an `environment_variables` list in
`portfolio.json` — the generator fails loudly if one is missing.

---

## Tips & troubleshooting

- **One repo at a time:** every pipeline script accepts `--only <id>`, e.g.
  `python scripts/release_all.py --repos-dir ../repos --only swiss-transport-mcp --build`.
- **`--help`** is available on every script.
- **`mcp-publisher: not recognized` / "not on PATH":** the CLI isn't installed or
  isn't on PATH — see the install section above.
- **`tar` missing on Windows:** present on Windows 10 (build 17063+) and 11;
  otherwise extract the `.tar.gz` with 7-Zip and keep `mcp-publisher.exe`.
- **`twine upload` fails with `'io.github...' is not a valid url`:** the
  `mcp-name` ended up in `[project.urls]`, where PyPI requires real URLs. The
  marker belongs in the README (step 1). Re-run `patch_mcp_name.py --write`
  (it moves the marker to the README and removes the bad URL), then re-release.
- **Everything stuck on `MISSING_MCP_NAME`:** you skipped step 2 (or the release
  didn't upload). The registry reads `mcp-name` from the *published* PyPI
  description, so a new release with the README marker must be live first.
