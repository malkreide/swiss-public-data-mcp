# Official MCP Registry entries

This directory holds one [`server.json`](https://github.com/modelcontextprotocol/registry)
draft per **active** portfolio server, ready to publish to the official MCP
Registry at <https://registry.modelcontextprotocol.io>. Getting listed there is
the single highest-leverage step for discoverability: it is the index that
clients (Claude Desktop, VS Code, Cursor, …) and third-party catalogues read.

> For the end-to-end operator walkthrough (install, auth, and running the
> publishing scripts in order, with Windows + macOS/Linux commands), see
> [`../RUNBOOK.md`](../RUNBOOK.md).

```
registry/<server-id>/server.json
```

These files are **generated** from [`portfolio.json`](../portfolio.json) — the
single source of truth — by [`scripts/generate_server_json.py`](../scripts/generate_server_json.py).
Do not edit them by hand; edit `portfolio.json` (or the generator) and rerun:

```bash
python scripts/generate_server_json.py          # regenerate
python scripts/generate_server_json.py --check   # CI: fail if drifted
```

Schema baseline: [`2025-12-11`](https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json).
Namespace: `io.github.malkreide/<server-id>` — validated for free via GitHub
OAuth, so no custom-domain DNS record is needed.

---

## What these drafts already get right

* Reverse-DNS `name`, `description`, and `repository` straight from `portfolio.json`.
* A `pypi` package launched via the `uvx` runtime hint (`stdio` transport).
* Credential servers' real `environmentVariables`, taken verbatim from each
  server's `environment_variables` in `portfolio.json`.
* Category/scope carried in `_meta` under the publisher-provided namespace.

## What you MUST reconcile per repo before publishing

Two values cannot be derived from `portfolio.json` and are intentionally left
as defaults:

| Field | Default in draft | Action |
|---|---|---|
| `packages[0].version` and top-level `version` | `0.1.0` | Set to the **actually published PyPI version**. |
| `packages[0].identifier` | the server id | Confirm the **PyPI distribution name**; fix if it differs from the repo name. |

The publish step (and the `mcp-name` ownership check below) is the gate that
catches a wrong version or identifier, so a bad draft fails loudly rather than
shipping silently.

---

## Publishing workflow (per server repo)

The registry validates ownership two ways at once: it checks that you control
the `io.github.malkreide` namespace (GitHub OAuth) **and** that the referenced
PyPI package declares the same registry name. Both must line up.

1. **Publish the package to PyPI** (if not already), and embed the registry name
   so the registry can verify ownership. In each server's `pyproject.toml`:

   ```toml
   [project.urls]
   "mcp-name" = "io.github.malkreide/<server-id>"
   ```

   (Equivalently, ship an `mcp-name: io.github.malkreide/<server-id>` line per the
   current registry docs.) Then build and upload the package as usual.

   This `[project.urls]` edit can be applied across all repos at once with
   [`scripts/patch_mcp_name.py`](../scripts/patch_mcp_name.py) (idempotent; dry
   run by default), so only the release builds remain manual:

   ```bash
   python scripts/patch_mcp_name.py --repos-dir ../repos --clone --write --commit --push
   ```

   Because PyPI metadata is immutable per version, the `mcp-name` link only
   reaches the registry via a **new release**. Cut one per repo with
   [`scripts/release_all.py`](../scripts/release_all.py) — it bumps the version
   (or tags VCS-versioned projects), builds, runs `twine check`, **verifies the
   built wheel actually advertises `mcp-name`** before uploading, and is a dry run
   by default:

   ```bash
   python scripts/release_all.py --repos-dir ../repos --build              # plan + build locally
   python scripts/release_all.py --repos-dir ../repos --commit --push --upload
   ```

2. **Copy the draft into the server repo root** as `server.json`, and update
   `version` / `identifier` as per the table above:

   ```bash
   cp registry/<server-id>/server.json /path/to/<server-id>/server.json
   ```

3. **Install the publisher CLI** (`mcp-publisher`) — see the registry repo for the
   current install command.

4. **Authenticate the namespace** via GitHub:

   ```bash
   mcp-publisher login github
   ```

5. **Publish:**

   ```bash
   cd /path/to/<server-id>
   mcp-publisher publish        # reads ./server.json
   ```

6. **Verify** the entry resolves:

   ```bash
   curl "https://registry.modelcontextprotocol.io/v0/servers?search=io.github.malkreide"
   ```

Repeat per server (a small shell loop over the 34 ids works well). New servers
flow automatically: add them to `portfolio.json`, rerun the generator, and the
draft appears here.

### Automating across all repos

[`scripts/publish_registry.py`](../scripts/publish_registry.py) drives the loop
above for the whole portfolio. It does **not** touch the committed drafts (those
stay pinned to `0.1.0` for CI); it resolves the published PyPI version per
package, writes a version-pinned **publish-ready** copy to `dist/registry/<id>/`,
and reports per-server blockers.

```bash
# Dry run: readiness table for all servers (no publishing, no repo changes).
python scripts/publish_registry.py

# Clone/refresh each repo as a sibling dir and publish the ready ones.
python scripts/publish_registry.py --repos-dir ../repos --clone --publish
```

It flags exactly what is missing before a server can publish:

* **`NOT_ON_PYPI`** — publish the PyPI package first.
* **`MISSING_MCP_NAME`** — the package's PyPI metadata does not yet declare the
  matching `mcp-name` (step 1 above). Add it and cut a release.

`--publish` requires `mcp-publisher` on `PATH` and an active
`mcp-publisher login github` session, and only ships servers reported `READY`.

---

## After listing — compounding the reach

Being in the official registry is what the major third-party catalogues
(Smithery, Glama, PulseMCP, MCP.so, …) ingest from, so a single publish
propagates outward. Two cheap multipliers:

* Add the standard discovery topics `mcp` / `model-context-protocol` to each
  repo (you already require `swiss-public-data-mcp`).
* Keep copy-paste client install snippets in each server's README so a registry
  visitor can run it in one step.
