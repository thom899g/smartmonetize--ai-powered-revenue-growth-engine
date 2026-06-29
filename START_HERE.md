# Start Here

Use this if you cloned SmartMonetize and want the fastest useful result.

## 1. Run The 60-Second Check

```bash
python3 -m smartmonetize.cli examples/saas_metrics.json --markdown report.md --json report.json
```

The output should answer one question:

```text
What is the fastest ethical move from attention to revenue evidence?
```

## 2. Replace The Example With Your Numbers

Copy `examples/saas_metrics.json` and change only the fields you know:

```json
{
  "product": "Your Product",
  "monthly_visitors": 0,
  "qualified_clicks": 0,
  "signups": 0,
  "paid_customers": 0,
  "average_price_usd": 49,
  "has_clear_offer": false,
  "has_checkout": false,
  "has_analytics": false,
  "owner_minutes_available": 30
}
```

Use public or anonymized numbers only.

## 3. Ask For A Free Fit Check

Open the request that matches your product:

- [General revenue triage](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=revenue_triage_audit.yml) for SaaS, web apps, demos, search traffic, signup funnels, or small products with attention but no paid conversion.
- [MCP/x402 endpoint mini-audit](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=mcp_x402_endpoint_audit.yml) for MCP servers, x402 endpoints, paid APIs, or agent-callable tools.
- [Agent/MCP trust-boundary audit](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=agent_mcp_trust_boundary_audit.yml) for agent frameworks, browser agents, memory systems, and automation products.

Include:

- one public URL
- one real signal
- the conversion boundary
- your desired outcome

Do not include secrets, payment details, private customer data, or confidential business data.

## 4. Paid Pilot Boundary

A GitHub issue is a free public fit check.

A paid pilot only happens after fit is explicit and both sides agree on the payment path.
