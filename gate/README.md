# Offline gate selection

`selection.json` opts this source revision into the offline variant gate. The
workflow retrieves the report and trusted attestation from Nexus under the exact
Git commit SHA. It rejects absent, changed or stale evidence.

The lab rehearsal uses synthetic products, queries and judgements. Its first
managed report was blocked because judged coverage was below policy. A separate
deterministic fixture can exercise the gate's decision states; fixture scores do
not measure model quality.
