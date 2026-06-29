# SmartMonetize v0.1.3

## Probe-to-payment diagnostic

- Refreshes the Ontario Protocol case study with live probe evidence: `x402_probe=3`, `402_responses=3`, `paid_calls=0`.
- Adds an explicit probe-to-payment gap section.
- Tightens the MCP/x402 mini-audit package around the moment where payment-aware clients reach HTTP 402 but do not complete payment.
- Extends the probe handoff draft with `http_402_responses`, `settle_successes`, and cheapest-paid-probe guidance.

Boundary: this release is external distribution and package clarity. It is not customer revenue.

# SmartMonetize v0.1.2

MCP/x402 endpoint-owner package release.

## Included

- Installable Python CLI: `smartmonetize`
- Deterministic revenue move ranking
- Example metrics file
- JSON and Markdown report output
- Sample revenue triage audit deliverable
- Public Ontario Protocol case study for products with discovery evidence but no buyer revenue
- Example MCP/x402 audit request so endpoint owners can paste safe public counters without sharing private data
- 5-minute self-service triage path for starred or curious visitors
- `$49` pilot audit offer and GitHub audit-request issue template
- `$199` MCP/x402 Endpoint Mini-Audit package for endpoint owners with directory or crawler attention

## Try It

```bash
python3 -m pip install -e .
smartmonetize examples/saas_metrics.json --markdown report.md --json report.json
```

## Buyer Path

- [Sample report](SAMPLE_REPORT.md)
- [5-minute self-service triage](QUICKSTART_TRIAGE.md)
- [Pilot offer](OFFER.md)
- [MCP/x402 Endpoint Mini-Audit](MCP_X402_ENDPOINT_AUDIT.md)
- [Example MCP/x402 audit request](EXAMPLE_MCP_X402_AUDIT_REQUEST.md)
- [Audit request issue form](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=revenue_triage_audit.yml)

## Boundary

This tool does not send outreach, create accounts, collect payment, promise revenue, or alter production systems. It helps founders decide the next revenue action from evidence.
