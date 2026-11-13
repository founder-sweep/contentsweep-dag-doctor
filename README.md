# DAG Doctor integration

<!-- contentsweep-proven-capability:begin -->
**Fully capable of supported exported Airflow 3.2/3.3 DAG and incident diagnosis through hosted MCP or free local tools.**

Proven exported Airflow incident diagnosis with evidence-linked findings. Repeatable hosted and free local demos show executor mismatch and context stops.

The repeatable executor-mismatch case produces DD-RUNTIME-006 with supporting evidence. Removing required run context produces needs_context without a hosted report debit. Both hosted and local execution passed.

[Inspect the result and repeat the demo](https://mcp.contentsweep.ai/dag-doctor/demos/exported-incident) · [Runnable package](demo/README.md) · [Capability and verification details](CAPABILITIES.md)
<!-- contentsweep-proven-capability:end -->


Connect to `https://mcp.contentsweep.ai/v1/dag-doctor/mcp/` with a verified organization's `X-API-Key`. Follow upload → preview → quote → start → poll → report. Keep the original quote/idempotency key on retries. Local stdio `diagnose_airflow_dag` is available through the standalone `dagdoctor-mcp` executable.

The hosted tool never accepts server paths. Upload actual relative Python source files and exported incident context. Use `examples/executor-mismatch/bundle.json` for an owned synthetic upload.

The adjacent server manifest is prepared release metadata. Availability, public Registry acceptance, sandbox payment qualification, live purchasing and independent adoption are separate facts; consult the product release receipt before claiming them.

## Free local tools

Python 3.12+ is required. Download the [wheel](https://mcp.contentsweep.ai/dag-doctor/download), verify it against the [SHA256 manifest](https://mcp.contentsweep.ai/dag-doctor/downloads/manifest.json), then install into a separate environment:

```sh
python3.12 -m venv .venv-dag-doctor
.venv-dag-doctor/bin/python -m pip install './contentsweep_dag_doctor-1.0.0-py3-none-any.whl[mcp]'
.venv-dag-doctor/bin/dagdoctor diagnose examples/pool-wait/source --runtime-context examples/pool-wait/incident.json --format json
```

The example paths above refer to the prepared distribution bundle. Local MCP command: `.venv-dag-doctor/bin/dagdoctor-mcp`; tool: `diagnose_airflow_dag`. This local-only wheel has no hosted billing code. Local findings may produce exit 2, missing context exit 3, invalid input exit 5.

## Examples and distribution

The checked-in `examples/` contain owned synthetic inputs and qualified reference reports. Install the maintained skill using the public-source instructions below. The engine and MCP connection are separate setup steps. `server.json` describes the hosted MCP interface; catalog acceptance and client qualification are tracked separately. Internal qualification does not establish customer adoption.

<!-- contentsweep-skill-distribution:begin -->
## Install the agent skill

Install this skill in the intended project, then choose the coding agents you use:

```sh
npx skills add founder-sweep/contentsweep-dag-doctor --skill diagnose-airflow-exports
```

For Claude Code, add the ContentSweep marketplace and install this product:

```sh
claude plugin marketplace add founder-sweep/contentsweep-supplier-feed-examples
claude plugin install contentsweep-dag-doctor@contentsweep
```

The marketplace contains Supplier Feeds, Data Quality Gate, Inspector, Schema Mapper, DAG Doctor and Deployment Fixer. Each plugin loads its existing product skill and companion references. Installation grants no upload, spending, business-rule approval or destination-write permission. MCP connections and runtime dependencies are configured separately using the bundled [agent setup](skills/diagnose-airflow-exports/references/hosted-workflow.md). Review the supported scope, privacy, free/local options and current hosted pricing before use.
<!-- contentsweep-skill-distribution:end -->

<!-- contentsweep-client-distribution:begin -->
## Gemini, Kilo, Cline and Cursor

Proven exported Airflow incident diagnosis with evidence-linked findings. Repeatable hosted and free local demos show executor mismatch and context stops.

Follow [client installation and recovery](CLIENTS.md). Native configuration examples, required settings, the existing skill and supported scope are included. Catalog submission and acceptance are recorded separately.
<!-- contentsweep-client-distribution:end -->

<!-- contentsweep-product-demo:begin -->
## Reproduce the product demo

Diagnose an exported Airflow executor mismatch.

[Public walkthrough](https://mcp.contentsweep.ai/dag-doctor/demos/exported-incident) · [Runnable package](demo/README.md) · [Native agent evidence](demo/agent-evidence.json)

Owned synthetic input, actual recorded output, expected stop cases, checksums, installation and pricing. The page reports native agent verification separately from deterministic MCP checks. Live hosted execution uses your own private credentials and explicit evaluation allowance.
<!-- contentsweep-product-demo:end -->
