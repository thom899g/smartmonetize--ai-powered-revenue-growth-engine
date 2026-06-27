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

Checked: `2026-06-27T13:27:42Z`.

- Verification reports: `total_reports=3099`, `ready=2934`, `close=55`, `needs_work=110`.
- Discovery counters: `developer_tool_hit=135`, `x402_probe=40`, `agent_crawler_hit=19`, `human_visit=24`.
- Conversion counters: `paid_call=0`, `readiness_subscription_intent=0`, `alert_subscriptions=0`, `third_party_submission=0`.
- x402 counters: `402_responses=40`, `paid_calls=0`, `settle_attempts=0`, `settle_successes=0`.
- Ledger boundary: one settled `0.01` USDC proof-of-life row exists, but it is self-funded and not customer revenue.
- Movement since the prior public snapshot: verification reports increased from `3093` to `3099`, ready reports increased from `2928` to `2934`, and latest-window attention increased across `developer_tool_hit`, `agent_crawler_hit`, `x402_probe`, and `human_visit`. Conversion counters stayed at zero.
- Counter hygiene: counter resets or drops are treated as telemetry hygiene until they are tied to buyer action; report growth, probe visibility, and human visits are useful attention signals, not customer revenue.

## Input Metrics

The local example file is [`examples/ontario_protocol_metrics.json`](examples/ontario_protocol_metrics.json):

```json
{
  "product": "Ontario Protocol",
  "monthly_visitors": 120,
  "qualified_clicks": 194,
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

The `qualified_clicks` value is a proxy for public machine attention in the current run: `x402_probe + agent_crawler_hit + developer_tool_hit`. Human visits are tracked separately because they are attention, but not enough by themselves to prove buyer intent. Treat counter resets or decreases as telemetry hygiene issues, not customer revenue or lost revenue.

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
