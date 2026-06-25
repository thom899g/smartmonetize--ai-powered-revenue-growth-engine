# Case Study: Ontario Protocol

This public case study shows how SmartMonetize handles a product with real distribution signals but no verified customer revenue yet.

## Public Signal Snapshot

- Product: Ontario Protocol
- Public surface: `https://ontarioprotocol.com`
- Attention signal: public directory and crawler activity around MCP/x402 discovery.
- Distribution signal: agent-tools.cloud lists Ontario Protocol's MCP endpoint as healthy with MCP/x402 support.
- Conversion gap: no verified buyer signup or third-party paid listing attempt from this channel yet.
- Boundary: do not count self-funded proof-of-life payments as customer revenue.

## Live Evidence Snapshot

Checked: `2026-06-25T19:13:23Z`.

- Verification reports: `total_reports=2972`, `ready=2808`, `close=55`, `needs_work=109`.
- Discovery counters: `x402_probe=8`, `agent_crawler_hit=3`, `developer_tool_hit=4`.
- Conversion counters: `paid_call=0`, `readiness_subscription_intent=0`, `alert_subscriptions=0`, `third_party_submission=0`.
- x402 counters: `402_responses=8`, `paid_calls=0`, `settle_attempts=0`, `settle_successes=0`.
- Ledger boundary: one settled `0.01` USDC proof-of-life row exists, but it is self-funded and not customer revenue.
- Movement since the prior public snapshot: verification reports increased by `6`, ready reports increased by `6`, `agent_crawler_hit` increased by `1`, and `developer_tool_hit` increased by `4`; conversion counters stayed at zero.

## Input Metrics

The local example file is [`examples/ontario_protocol_metrics.json`](examples/ontario_protocol_metrics.json):

```json
{
  "product": "Ontario Protocol",
  "monthly_visitors": 120,
  "qualified_clicks": 15,
  "signups": 0,
  "paid_customers": 0,
  "average_price_usd": 49,
  "has_clear_offer": true,
  "has_checkout": false,
  "has_analytics": true,
  "owner_minutes_available": 20
}
```

These are intentionally conservative rough numbers. They are not private analytics exports.

The `qualified_clicks` value is a proxy for public machine attention in the current run: `x402_probe + agent_crawler_hit + developer_tool_hit`. Treat counter resets or decreases as telemetry hygiene issues, not customer revenue.

## Run It

```bash
python3 -m smartmonetize.cli examples/ontario_protocol_metrics.json --markdown ontario-triage.md --json ontario-triage.json
```

## Current Recommendation

SmartMonetize should choose:

```text
Add a direct paid pilot CTA
```

Why: Ontario has public discovery evidence and working x402 surfaces, but the next revenue step is not another internal system. It is a direct paid pilot path that converts a directory crawler, endpoint owner, or developer into a concrete request.

## Best Buyer-Facing Test

Offer:

```text
Get an x402/MCP endpoint readiness triage.

Send a public endpoint or repo. Receive the top 3 fixes that make it easier for agent directories and payment-aware clients to discover, price, and safely call your service.
```

Valid evidence:

- inbound issue/request
- directory recrawl that fills missing fields
- endpoint owner asks for a mini-check
- paid x402 listing attempt
- payment discussion
- payment

Invalid evidence:

- local report
- self-funded test payment
- generated dashboard
- another README edit

## Kill / Scale / Revise Rule

- Scale if a developer opens an audit request, asks about a paid check, or triggers a real paid call.
- Revise if directories keep crawling but no owner action appears.
- Kill this angle if the watch window closes with no external signal after the paid pilot CTA is visible.

## Request The Same Audit

If your product has attention but no paid conversion, open a request:

[Revenue Triage Audit Request](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=revenue_triage_audit.yml)

For MCP/x402 endpoint owners specifically, use the [`MCP/x402 Endpoint Mini-Audit`](MCP_X402_ENDPOINT_AUDIT.md). It is the sharper package for turning directory/crawler discovery into a buyer-safe endpoint proof and action plan.
