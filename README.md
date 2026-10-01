# Search delivery demonstration

Synthetic search API; immutable Nexus releases. This is a fixture repository for the lab reference CI/CD.

## Offline variant gate

`app/variants.py` selects a named ranking configuration through `X-Lab-Variant` and echoes its identity and digest in the public Search API response. `SEARCH_VARIANTS_JSON` names one required runtime default. The evaluation baseline is chosen separately in the frozen variant set.

To gate a source PR, commit `gate/selection.json` with a `variant-gate-selection` object (`schema_version: 1`) and a non-empty `selected` list. Each selected item names a `variant` and an `intent` of `ranking-change` or `preserve-results`. The selection does not contain its own Git SHA. CI builds the exact PR commit and then loads `variant-gates/<source SHA>/report.json`, `attestation.json` and optional `approvals.json` from the Nexus raw repository. `ci/variant_gate.py` checks the pinned policy, signed evidence, coverage, metric deltas and result changes. Missing or invalid evidence fails the declared gate.

The lab operator uses `lab/variant_gate_issue.py` in the reference repository to attest a complete frozen report for the source SHA. `ci/variant_gate_store.py publish-evidence` publishes the report and attestation to Nexus. A bounded negative result needs an administrator's signed exception with a reason; `ci/variant_gate_store.py publish-approval` adds that receipt. Rerun the check for the same commit after publication. The approval does not change the measured score. The [reference guide](https://github.com/FinnNk/ephemeral-elastic-search-stack/blob/main/docs/variant-evaluation.md) describes the full synthetic capture and judgement path.

Temporary documentation-exemption verification.
