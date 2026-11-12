# DAG Doctor: coding-agent setup

Diagnose exported Airflow 3.2/3.3 incidents with evidence and explicit coverage gaps.

## Runtime and credentials

Create or reuse a verified organization at https://mcp.contentsweep.ai/dag-doctor, activate this product, and supply its private organization key as `CONTENTSWEEP_DAG_DOCTOR_API_KEY`. Initialization and tool listing require the key. Review upload permission, the quote and the evaluation cost before starting a hosted job. Use the original quote and idempotency key after an uncertain response.

## Gemini CLI

Install the extension from this repository:

```sh
gemini extensions install https://github.com/founder-sweep/contentsweep-dag-doctor --ref main
```

The explicit branch selects the integration source rather than an older Python runtime release archive. Provide the requested setting in the native installation prompt. API keys are sensitive settings. The extension supplies the existing skill and default MCP connection; it does not approve tool calls or spending. For a project-managed connection, merge the Gemini example from `client-configs/gemini.json` into the intended profile.

## Kilo

Use the published marketplace entry when available, or merge `client-configs/kilo.json` into your private user-level Kilo CLI configuration and install the existing skill. Alternatively set `KILO_CONFIG` to the absolute path of an explicitly trusted private configuration file. Kilo CLI rejects environment substitutions in untrusted project configuration and drops MCP entries with variable-bearing project headers; keep the supplied environment-based credentials in user-level configuration. The editor marketplace installs its prompted values into private MCP settings. The catalog entry includes a companion skill; companion installation requires a client version supporting that feature. Review prerequisites before installation.

## Cline

Ask Cline to follow this README and `llms-install.md`. Merge the entry in `client-configs/cline.json` into the editor extension's MCP settings and provide the named setting privately. Cline editor 4.1.26 supports `${env:NAME}` interpolation. Make those variables available in the client launch environment, or fill the actual values directly in the client's private MCP settings. Restart the client after changing its launch environment. The hosted editor example selects `streamableHttp` explicitly. Keep tool approvals enabled.

Cline CLI 3.0.74 stores its connection under a `transport` object. Use its native command to write that schema instead of copying the editor JSON into a CLI profile. With the required private setting(s) available in the launch environment:

```bash
cline mcp add contentsweep-dag-doctor --yes --transport streamable-http --header "X-API-Key: ${CONTENTSWEEP_DAG_DOCTOR_API_KEY}" "https://mcp.contentsweep.ai/v1/dag-doctor/mcp/"
```

For the local alternative, use `cline mcp add contentsweep-dag-doctor-local --yes --transport stdio -- "${CONTENTSWEEP_DAG_DOCTOR_MCP_COMMAND}"`. Choose the intended hosted or local tool explicitly. For an isolated CLI profile, retain its `--config`, `--data-dir` and `--hooks-dir` options on configuration commands. Start a fresh Cline CLI task after adding the server so the model discovers its new tools. Copy the existing skill directory with every relative resource into the project's `.cline/skills/` directory; manual file copying does not require a second skill-install command. Verify an actual MCP result after setup.

## Cursor

Install the Cursor plugin from the marketplace or load this repository as a local plugin for development. Configure its declared variable in the plugin settings. The root `mcp.json` is the native plugin connection definition; the copy in `client-configs/cursor.json` is for a manually managed connection. For the manual copy, use Cursor's documented environment interpolation in place of the plugin variable. Preserve unrelated entries. With Cursor CLI, place local environments at absolute paths without spaces: the current CLI splits a no-argument stdio command containing spaces. A locally created executable symlink at a path without spaces is also suitable; it must point to the verified installed product executable. In native Cursor 3.29.15, Inspector's project-scoped Configure action returned "Plugin not installed". The tested recovery was to select Add for Myself, remove the failed project scope, save the declared variables in the private plugin configuration, and use the MCP server's Reload action. Verify Connected and the expected tools before running a task. This recovery does not require a second manually configured connection.

## Skill and first task

Read [diagnose-airflow-exports](skills/diagnose-airflow-exports/SKILL.md) and its relative references. Use the repository-owned synthetic example first and inspect the substantive result, not just execution success. Fixture approval never authorizes customer uploads, business meanings, purchases or downstream writes. Read the owned example `bundle.json` before a hosted upload and pass its parsed properties as MCP arguments, including the `files` mapping. Each file name and content must come from that reviewed bundle. For a local DAG example, `incident.json` is beside the `source/` directory; pass that complete incident object as `runtime_context`.

## Price and supported scope

Five trials per verified organization; $20/20 hosted reports. Free local tools. Missing context, unsupported input and platform failures consume no credit.

Exported Airflow 3.2/3.3 DAG source and incident context. No live production access, imported customer code or automatic fixes.

## Free local alternative

Download and verify the local wheel using the official README instructions. Install into a dedicated Python 3.12+ environment and set `CONTENTSWEEP_DAG_DOCTOR_MCP_COMMAND` to the absolute `dagdoctor-mcp` executable path. Use the matching `client-configs/*-local.json` entry instead of the hosted entry, preserving unrelated settings. Kilo offers this as a separate installation method. The skill remains the same; local analysis does not create hosted history or consume hosted credits.

## Preserve the reviewed bundle

Keep every filename, dictionary key and source byte unchanged. A filename such as `daily_load.py` must retain its dot and extension; replacing punctuation changes the input. If a model reconstructs the bundle incorrectly through the MCP upload arguments, stop instead of trying renamed variants. The client's reviewed file-transfer tool can send the original JSON bundle directly to the existing HTTPS upload endpoint, with the private key available in its launch environment:

```bash
BUNDLE_FILE="/absolute/path/to/owned/bundle.json"
curl --fail-with-body --silent --show-error --request POST "https://uploads" \
  --header "Content-Type: application/json" \
  --header "X-API-Key: ${CONTENTSWEEP_DAG_DOCTOR_API_KEY}" \
  --data-binary "@${BUNDLE_FILE}"
```

Verify the source file hash before transfer. Use the returned upload ID with the native MCP preview, quote, execution, report and retry tools. Uploading does not start an evaluation. This transfer requires authorization for the exact source and exported context; never print the key or execute the uploaded code.

## Recovery and removal

Keep private keys out of source control and command history. Remove only this product's plugin/server/owned companion skill. Keep unrelated tools and settings. Kilo 7.8.27's native skill Remove action deletes `SKILL.md` and leaves companion files. After native removal, preview cleanup of this exact skill directory using the supplied ownership manifest:

```bash
python scripts/remove-owned-agent-skill.py --skill-dir "/absolute/path/to/.kilo/skills/diagnose-airflow-exports"
```

Review the matching paths, then repeat with `--apply` to remove only unchanged owned companion files. The helper refuses an active skill entry or a symlinked skill directory, and preserves modified files, unknown files and other skills. It does not edit client configuration. When names conflict, inspect the client's selected source path before installing or removing a skill. Client installation, marketplace acceptance, recommendations and paid adoption are separate outcomes.
