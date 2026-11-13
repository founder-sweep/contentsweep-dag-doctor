# Diagnose an exported Airflow executor mismatch

Find DD-RUNTIME-006 in supplied evidence without connecting to Airflow. Remove the run context and keep the outcome unresolved without debit.

Owned synthetic example. Recorded results are clearly separated from live execution. Installing a skill does not install its runtime or authorize spending or uploads.

## Inspect the evidence

Read `manifest.json`, `expected.json`, and the fixtures before running. The walkthrough covers executor-mismatch, executor-mismatch-missing-context. Results come from actual product MCP calls, not simulated responses. The free public page and downloads require no sign-in.

## Reproduce with your agent

Read the existing `diagnose-airflow-exports` skill and its companion setup/tool references. Then follow `AGENT_PROMPT.md`. Create a dedicated Python 3.12+ environment and install `mcp>=2.3,<3`. Configure CONTENTSWEEP_DAG_DOCTOR_API_KEY privately in your environment; never paste its value into prompts, command arguments, URLs or source control.

These commands are qualified on macOS and Linux. Follow [client setup](https://github.com/founder-sweep/contentsweep-dag-doctor/blob/main/CLIENTS.md) for runtime installation. Use that environment’s Python to run the demo.

For deterministic verification from this repository root:

```sh
python demo/run.py --mode hosted --max-units 1 --output demo-results
```

The hosted allowance explicitly authorizes at most 1 evaluations of these named synthetic cases. Review the supplied field decisions before approving them. It grants no permission for customer files, purchases, destination writes, source edits or cloud actions. Hosted keys are your own; local analysis needs no hosted key.

Reuse the same output directory and allowance after an uncertain response. `resume.private.json` preserves quote/key/job identities before dispatch. Keep it private. Never start a new run merely because polling timed out. Changed customer data needs its own review and authorization. A completed rejection, block or warning can be billable as documented for this product.

## Interpret the result

Inspect `result.json` for assertions, complete reports and actual tool discovery. Expected stop cases are part of a passing demo. A deterministic runner is not a native agent completion. Machine-generated IDs, timestamps and local paths may differ; business values, coverage and accounting must agree.

Exported Airflow 3.2/3.3 DAG source and incident context. No live production access, imported customer code or automatic fixes.

## Price and next step

Five trials per verified organization; $20/20 hosted reports. Free local tools. Missing context, unsupported input and platform failures consume no credit.

[Read the full walkthrough and setup](https://mcp.contentsweep.ai/dag-doctor/demos/exported-incident) · [Product and current terms](https://mcp.contentsweep.ai/dag-doctor)

Keep local/free options separate from optional hosted purchases. This example performs no purchase. Reports are bounded evidence, not runtime certification or proof of customer outcomes.

## Free local alternative

Verify version 1.0.0 against SHA256 `4c70e010790e9e1b18f285f8348ca2e6333c02428673d75bdc8f57b45372da4a` before installation. Then use:

```sh
python demo/run.py --mode local --command /ABSOLUTE/TO/ENV/bin/dagdoctor-mcp --output local-demo-results
```

Local reports expose engine findings; hosted reports add support/accounting semantics. Compare substantive evidence and coverage, not wrapper fields.

## Preserve original bytes in a native agent session

Some clients reconstruct file contents or rewrite object keys. Use this reviewed helper through the agent’s native shell tool to upload the exact checksum-bound fixtures, then continue with the product’s native MCP review, approval, quote, evaluation, report and retry tools:

```sh
python demo/transfer.py --confirm-upload --output demo-uploads/uploads.private.json
```

It uploads only the bundled synthetic files and prints owned upload IDs. It performs no approval, evaluation, purchase or destination write. Keep its identity file private and reuse it after an interruption. This mixed file-transfer/MCP workflow is disclosed in the native evidence.

<!-- demo-specific-walkthrough -->
## Follow the exported evidence

`DD-RUNTIME-006` links the selected KubernetesExecutor to a topology containing only LocalExecutor. Removing run_id produces `needs_context`; no report credit is consumed. The [recorded free local result](https://mcp.contentsweep.ai/dag-doctor/demos/exported-incident/local-result.json) exposes the same engine evidence, while hosted reports add support/accounting metadata. Also inspect the existing [pool-wait example](https://github.com/founder-sweep/contentsweep-dag-doctor/tree/main/demo/fixtures/pool-wait) and [branch-join example](https://github.com/founder-sweep/contentsweep-dag-doctor/tree/main/demo/fixtures/branch-join). Neither requires an Airflow connection.
