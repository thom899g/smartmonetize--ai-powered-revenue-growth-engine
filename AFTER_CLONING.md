# After Cloning SmartMonetize

If you cloned this repo because your product has attention but no paid conversion, this is the fastest path.

## 1. Run The Local Triage

```bash
python3 -m smartmonetize.cli examples/saas_metrics.json --markdown report.md --json report.json
```

For MCP, x402, paid API, or agent-callable endpoint work, start with:

- [MCP/x402 Endpoint Mini-Audit](MCP_X402_ENDPOINT_AUDIT.md)
- [Agent/MCP Trust Boundary Audit](AGENT_MCP_TRUST_BOUNDARY_AUDIT.md)
- [Ontario Protocol case study](CASE_STUDY.md)

## 2. Decide Whether You Need A Fit Check

Open a public fit-check issue only if you can provide:

- one public URL,
- one real signal,
- one conversion boundary,
- and one desired outcome.

Good signals:

- repo stars, forks, clones, or issue activity
- directory rows or crawler fetches
- search impressions or clicks
- demo usage
- x402 probes or HTTP 402 responses
- free-tool usage

Not enough by itself:

- "looks promising"
- a private hunch
- generated dashboards
- self-funded test payment
- a clone with no product signal

## 3. Pick The Right Request

- [Agent/MCP Trust Boundary Audit request](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=agent_mcp_trust_boundary_audit.yml) for agent frameworks, MCP servers, browser agents, memory systems, and agent-callable tools.
- [MCP/x402 Endpoint Mini-Audit request](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=mcp_x402_endpoint_audit.yml) for MCP/x402 endpoints, paid APIs, and agent-commerce surfaces.
- [General Revenue Triage Audit request](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=revenue_triage_audit.yml) for small products with traffic, signups, demos, or search attention but no clear paid conversion.

## 4. Keep It Public And Safe

Do not include:

- passwords
- API keys
- private customer data
- payment details
- confidential business data
- private admin URLs

## 5. Paid Pilot Boundary

Opening an issue is a free public fit check. A paid pilot only happens after the fit is explicit and both sides agree on the payment path.

No revenue is promised or guaranteed.
