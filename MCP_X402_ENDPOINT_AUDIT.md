# MCP/x402 Endpoint Mini-Audit

Status: pilot package.

Price: `$199` for one public MCP or x402 endpoint.

## Who It Is For

Builders with a public MCP, paid API, x402 service, or agent-callable endpoint that already has some discovery signal but is not converting into trusted calls, listings, or paid usage.

Good fit:

- agent/tool directory listing exists but has missing metadata
- MCP endpoint is callable but buyers do not know what it costs
- x402 manifest exists but chain, currency, payee, or facilitator fields are unclear
- public crawler or developer traffic exists but no owner inquiry or paid call follows
- a founder needs a buyer-safe proof packet before asking agents or directories to trust the endpoint

Fastest current fit: an endpoint has crawler or directory hits, public x402/MCP metadata, and `paid_calls=0`. The mini-audit starts by finding the smallest public trust or handoff gap between machine discovery and a real buyer action.

If report counts, developer-tool hits, crawler fetches, or x402 probes keep rising while `paid_calls`, listing submissions, and subscription intent stay at zero, treat that as a conversion problem: the endpoint is being inspected, but the buyer-safe next action is not obvious enough yet.

Developer-tool attention is enough for the free fit check when it is public and concrete. If your latest window shows `developer_tool_hit`, `x402_probe`, MCP manifest fetches, or directory crawler activity but still has `paid_calls=0`, open the issue with those counters and ask for the one action that should come before outreach, ads, or a payment-link change.

Benchmark/API visitor attention is also enough for the free fit check when the visited endpoint is public. If people or crawlers are hitting benchmark rows, comparison APIs, report APIs, or paid-endpoint metadata while `paid_calls=0`, submit the visited paths, durable report totals, latest-window events, and the current buyer-action boundary. The first audit question becomes: what public next step should a benchmark reader take before paying, listing, or trusting the endpoint?

If some counters reset while durable totals keep rising, do not treat the reset as lost demand. Submit both views: durable totals such as `total_reports` and `ready_reports`, then the latest-window counters and any prior-window counters that show crawler, probe, or developer-tool attention.

Bad fit:

- private endpoints that require admin credentials
- legal, tax, investment, or compliance advice
- guaranteed listing acceptance
- guaranteed revenue
- mass outreach or automated submissions

## What You Get

One concise endpoint-owner packet:

1. Public discovery read: what agents, crawlers, and directories can see.
2. Payment-readiness read: HTTP 402, x402 manifest, chain, currency, payee, facilitator, and price boundaries.
3. Buyer-trust gap list: the top blockers that make an agent or directory hesitate.
4. One shippable endpoint-owner action plan.
5. One follow-up measurement window: what would count as a real signal after the fix.

## What To Provide

Only public or non-sensitive inputs:

```json
{
  "product": "Example MCP Service",
  "endpoint": "https://example.com/mcp",
  "x402_manifest": "https://example.com/.well-known/x402.json",
  "target_directory": "agent-tools, MCP registry, Bazaar-style marketplace, internal agent buyer",
  "known_signal": "crawler hit, directory listing, star, issue, search impression, demo click",
  "desired_outcome": "accepted listing, paid call, buyer-safe readiness proof, or owner inquiry"
}
```

Do not send passwords, private customer data, API keys, wallet secrets, payment details, or private admin URLs.

If your signal is machine attention with no buyer action yet, paste the smallest public snapshot that proves the gap:

```text
Endpoint:
x402 manifest:
MCP manifest:
Current signal: total_reports=3075, ready_reports=2910, latest_window_developer_tool_hit=4
Conversion boundary: paid_calls=0, listing submissions=0, subscriptions=0, buyer replies=0
Desired outcome: one trusted next action for an agent, directory, or endpoint owner
```

For benchmark/API visitor evidence, include paths instead of private analytics:

```text
Visited paths: /api/benchmarks/<slug>, /benchmarks/<slug>, /api/benchmarks/compare
Current signal: human_visit=4, agent_crawler_hit=3, x402_probe=8
Durable totals: total_reports=3129, ready_reports=2961
Conversion boundary: paid_calls=0, readiness_subscription_intent=0, alert_subscriptions=0
Desired outcome: one public next step for a benchmark reader before payment or listing
```

The audit starts from that boundary. It does not need private analytics, wallet secrets, admin access, or a live payment link.

## Deliverable Shape

The mini-audit is intentionally practical:

```text
Endpoint: https://example.com/mcp
Signal: directory crawler found it, but paid usage is zero.
Top blocker: x402 price/currency/facilitator fields are not visible to the directory.
Fastest fix: expose top-level chain, currency, price_min, price_max, payTo, and facilitator_url.
Validation: rerun directory/card check and watch for accepted listing, crawler recrawl, owner inquiry, or paid call.
Boundary: no guarantee of listing acceptance or revenue.
```

## How To Start

Open the dedicated MCP/x402 audit request issue and paste one public signal snapshot:

[MCP/x402 Endpoint Mini-Audit Request](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=mcp_x402_endpoint_audit.yml)

If you are unsure what to paste, copy the safe public structure in [Example MCP/x402 Audit Request](EXAMPLE_MCP_X402_AUDIT_REQUEST.md).

After a real endpoint-owner issue exists, the first public reply should stay inside the [First Response MCP/x402 Audit Skeleton](FIRST_RESPONSE_MCP_X402_AUDIT_SKELETON.md): public evidence only, one buyer-trust gap, one safe next action, and no payment discussion unless fit is explicit.

If the only current signal is machine inspection, use the [MCP/x402 probe handoff draft](MCP_PROBE_HANDOFF_DRAFT.md) first. It keeps the response bounded to public counters, the zero buyer-action boundary, and one readiness note before any outreach, listing submission, deployment, or payment-path change.

This repository does not collect payment automatically. A paid pilot only happens after a real request and an explicitly agreed payment path.

## Current Public Example

The Ontario Protocol case study shows the pattern:

- public MCP/x402 discovery signal exists
- self-funded rail proof exists
- directory metadata can still be incomplete or stale
- no buyer revenue is counted until there is a real external signal

Read: [Ontario Protocol case study](CASE_STUDY.md)
