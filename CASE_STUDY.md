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

Checked: `2026-06-29T18:25:59Z`.

- Verification reports: `total_reports=3261`, `ready=3090`, `close=61`, `needs_work=110`.
- Discovery counters: `developer_tool_hit=13`, `agent_crawler_hit=6`, `x402_probe=24`, `human_visit=10`.
- Conversion counters: `paid_call=0`, `readiness_subscription_intent=0`, `alert_subscriptions=0`, `third_party_submission=0`.
- x402 counters: `402_responses=24`, `paid_calls=0`, `settle_successes=0`.
- Ledger boundary: one settled `0.01` USDC proof-of-life row exists, but it is self-funded and not customer revenue.
- Movement since the prior public snapshot: verification reports increased from `3255` to `3261`, ready reports increased from `3084` to `3090`, developer-tool hits increased from `2` to `13`, x402 probes increased from `2` to `24`, HTTP 402 responses increased from `2` to `24`, and human visits increased from `4` to `10`. Agent-crawler hits moved from `9` to `6`, which is treated as reset-prone telemetry rather than buyer rejection. Conversion counters stayed at zero.
- Directory state: the live agent-buyer guide, MCP manifest, x402 manifest, and 402 payment challenge are reachable.
- Counter hygiene: one `x402_probe` in this snapshot came from an internal verification curl, so the safest interpretation is not "buyer demand proved." The valid public signal is that developer/tool attention is present while buyer-action counters are still zero.

## Input Metrics

The local example file is [`examples/ontario_protocol_metrics.json`](examples/ontario_protocol_metrics.json):

```json
{
  "product": "Ontario Protocol",
  "monthly_visitors": 53,
  "qualified_clicks": 43,
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

The `qualified_clicks` value is a proxy for public machine attention in the current run: `x402_probe + agent_crawler_hit + developer_tool_hit`. The `monthly_visitors` value is a conservative current-window attention proxy: machine attention plus human visits. Treat counter resets or decreases as telemetry hygiene issues, not customer revenue or lost revenue. Verification calls can contaminate probe counters, so SmartMonetize keeps the zero-revenue boundary visible instead of pretending every probe is a buyer.

## Current Probe-To-Payment Gap

The strongest current Ontario signal is not a star, a report, or a dashboard. It is this boundary:

```text
developer_tool_hit=13
agent_crawler_hit=6
x402_probe=24
402_responses=24
paid_calls=0
settle_successes=0
```

That means machine discovery is still happening and payment-aware clients can reach the 402 boundary, but nobody has completed a customer paid call yet. The SmartMonetize diagnosis is:

```text
Discovery works enough to trigger tool and probe attention.
The next revenue question is why payment-aware clients stop at the 402 boundary instead of completing a paid call or requesting the free endpoint-owner mini-check.
```

The immediate mini-audit focus should be the directory-to-buyer bridge:

1. Is the 402 challenge easy for an agent to parse?
2. Does the manifest make price, network, asset, facilitator, and purpose obvious?
3. Is there a free can-pay or readiness preflight before spend?
4. Does the response explain what evidence the paid call returns?
5. Does the public directory row crawl the canonical `.json` manifest and reachable buyer guide?
6. Is the cheapest paid action clearly low-risk enough to try?

For Ontario, the owned public fix was to expose an agent-buyer guide and release it publicly:

- Agent buyer guide: `https://ontarioprotocol.com/.well-known/agent-buyer.json`
- Lowest-friction paid path: `GET /api/x402/reputation/<agent_id>` at `0.001 USDC`
- Endpoint-owner path: `POST /api/x402/list-service` at `0.50 USDC`
- Public release: `https://github.com/thom899g/ontarioprotocol/releases/tag/v0.1.1`

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
- Revise if directories keep crawling or developer-tool hits keep rising but no owner action appears.
- Kill this angle if the watch window closes with no external signal after the paid pilot CTA is visible.

## Request The Same Audit

If your product has attention but no paid conversion, open a request:

[Revenue Triage Audit Request](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=revenue_triage_audit.yml)

For MCP/x402 endpoint owners specifically, use the [`MCP/x402 Endpoint Mini-Audit`](MCP_X402_ENDPOINT_AUDIT.md). It is the sharper package for turning directory/crawler discovery into a buyer-safe endpoint proof and action plan.
