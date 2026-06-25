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

Open the same audit request issue and mention `MCP/x402 Endpoint Mini-Audit`:

[Revenue Triage Audit Request](https://github.com/thom899g/smartmonetize--ai-powered-revenue-growth-engine/issues/new?template=revenue_triage_audit.yml)

This repository does not collect payment automatically. A paid pilot only happens after a real request and an explicitly agreed payment path.

## Current Public Example

The Ontario Protocol case study shows the pattern:

- public MCP/x402 discovery signal exists
- self-funded rail proof exists
- directory metadata can still be incomplete or stale
- no buyer revenue is counted until there is a real external signal

Read: [Ontario Protocol case study](CASE_STUDY.md)
