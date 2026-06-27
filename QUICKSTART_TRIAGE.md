# 5-Minute Revenue Triage

Use this when your product has attention but no paid conversion yet. It is designed for public or anonymized numbers only.

## 1. Copy The Metrics Template

Create `my-product.json`:

```json
{
  "product": "My Product",
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

Use rough numbers. Do not include passwords, API keys, private customer data, payment details, or confidential business data.

## 2. Run The Triage

```bash
python3 -m pip install -e .
smartmonetize my-product.json --markdown my-product-triage.md
```

Or run without installing:

```bash
python3 -m smartmonetize.cli my-product.json --markdown my-product-triage.md
```

## 3. Read The Decision

The useful output is not a long report. It is the first concrete move:

- `kill`: stop this channel because evidence is too weak
- `revise`: sharpen offer, CTA, proof, or target
- `scale`: there is enough signal to push the next approved test

## 4. Compare Against The Samples

Read [`SAMPLE_REPORT.md`](SAMPLE_REPORT.md) before requesting help. A good request has:

- a public URL or repo
- one attention signal
- one conversion problem
- a clear owner-time limit
- no private data

For a real public-product pattern, read [`CASE_STUDY.md`](CASE_STUDY.md). It shows a product with directory/crawler evidence, working payment-aware surfaces, and still no verified customer revenue.

If your product is an MCP, x402, paid API, or agent-callable endpoint, read [`MCP_X402_ENDPOINT_AUDIT.md`](MCP_X402_ENDPOINT_AUDIT.md) before requesting help. That package is more specific than the generic revenue triage audit.

For MCP/x402 endpoints, a developer-tool hit, manifest fetch, x402 probe, directory crawler fetch, or public repo star is enough for the free fit check when paired with the current buyer-action boundary. Use the dedicated [`MCP/x402 Endpoint Mini-Audit Request`](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=mcp_x402_endpoint_audit.yml), not the generic form, and paste counters such as `developer_tool_hit=4` with `paid_calls=0`.

## 5. Request A Pilot Audit

If your product has real attention and the triage points to a paid-test gap, open the audit request:

[Revenue Triage Audit Request](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=revenue_triage_audit.yml)

The current pilot is `$49` for the first 3 qualified audits. Payment is not collected automatically. A paid pilot only happens after a real request and an explicitly agreed payment path.

## Valid Signals

Useful market evidence:

- reply
- issue opened
- signup
- payment discussion
- payment
- qualified rejection
- no-reply after a defined window

Not enough by itself:

- a star
- a local report
- a dashboard
- a vague "looks promising"
