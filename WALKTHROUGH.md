# DAG Doctor marketing walkthrough

Prepared November 12, 2026. The hosted product is live; the new distribution bundle and copy below are ready for review. Examples are synthetic, use the actual engine and do not execute Airflow. This file is included as `WALKTHROUGH.md` in the bundle.

## Position and offer

Diagnose exported Airflow 3.2/3.3 incidents without connecting an agent to production. Return evidence-linked signatures, missing context and a next investigation step. Local CLI/MCP are free. Hosted saved diagnoses have five trials per verified organization, then $20/20 reports. Completed supported diagnoses use one report; incomplete/unsupported/platform failures consume none. No subscription or automatic replenishment.

Lead audience: engineers maintaining Airflow DAGs who can export source and task context. The value is a bounded exported-evidence workflow and saved delivery, with no live Airflow connection. Do not claim measured accuracy, time saved, incident prevention or superiority over an existing script.

## Reproduce the three cases

Install the checksum-verified local wheel as described in `README.md`. Run from this bundle's root:

```sh
dagdoctor diagnose examples/pool-wait/source --runtime-context examples/pool-wait/incident.json --format json
dagdoctor diagnose examples/branch-join/source --runtime-context examples/branch-join/incident.json --format json
dagdoctor diagnose examples/executor-mismatch/source --runtime-context examples/executor-mismatch/incident.json --format json
dagdoctor diagnose examples/pool-wait-missing-context/source --runtime-context examples/pool-wait-missing-context/incident.json --format json
```

| Case | Actual expected evidence | Interpretation |
| --- | --- | --- |
| Pool wait | `DD-RUNTIME-004` and exported pool/log markers | Investigate capacity; no claim that more slots alone resolves the incident. |
| Branch join | `DD-TRIGGER-001` static graph finding, `DD-RUNTIME-001` upstream state | Review join semantics and the first failed upstream task. Their coexistence does not prove the branch rule caused this failure. |
| Executor mismatch | `DD-RUNTIME-006`, selected executor absent from exported topology | Confirm the topology export and worker configuration. No live executor was queried. |
| Each missing-context variant | `needs_context`, missing `run_id`, incomplete supported coverage | Ask for evidence; do not present a complete diagnosis or consume a hosted report. |

Each folder contains `bundle.json`, `incident.json`, `source/`, and `report.json`. Findings can cause local exit 2; missing context exits 3. Expected nonzero analysis outcomes are not installation failures. Confidence is heuristic. Reports describe static/exported evidence rather than observed scheduler execution.

## Hosted demonstration

Open the [workspace](https://mcp.contentsweep.ai/dag-doctor/app?source=technical-demo&channel=owned&asset=airflow-export-cases&campaign=dag-launch-v1). Verify email, activate DAG Doctor, load a case's `bundle.json`, review coverage and explicitly start one report. Download the result and keep its receipt. The missing-context variant consumes none. Source/logs expire in 24h and reports in 7d; raw customer exports must not be used in public demonstrations without permission.

## Draft launch copy

**Short post:** I built DAG Doctor for exported Airflow incidents: give it DAG source plus task context and get an evidence-linked diagnosis with uncertainty left visible. The worked cases cover pool waits, branch-join review and executor mismatch, including missing-context outcomes. It never connects to production or executes uploaded code. Local tools are free; hosted saved reports have five organization trials, then $20/20. I’m the founder of ContentSweep. [Try the synthetic example](https://mcp.contentsweep.ai/dag-doctor?source=founder-post&channel=community&asset=airflow-export-cases&campaign=dag-launch-v1).

**Technical contribution angle:** Walk through one pool-wait export, show the specific signature and incomplete-context counterexample, and ask what exported evidence is hardest to collect. Include the free local route first and disclose founder affiliation. Adapt to the actual community's rules before posting. No destination or message has been submitted by this preparation.

## First acquisition cycle

Use campaign `dag-launch-v1`; preserve `source`, `channel`, `asset` and `campaign` through the current signup flow. Prepare one technical example placement and a small manually qualified Airflow operator batch in the existing central review. Exact recipients/messages require their existing campaign approval; this packet sends nothing.

Record placement views/clicks only where observable, verified organizations, completed supported trials, missing-context outcomes, purchases/refunds, repeat purchased use and support time. Internal qualification is excluded. Missing attribution is unknown. Review after seven days of actual distribution; decide whether to improve evidence collection or positioning from observed completion and purchase friction. No paid ads or new recurring scheduler is needed to start.
