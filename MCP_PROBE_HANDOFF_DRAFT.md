# MCP/x402 Probe Handoff Draft

Use this when a public MCP or x402 endpoint is being inspected by developer tools, crawlers, or x402 probes, but no paid call, subscription intent, buyer reply, or third-party submission has happened yet.

This is not outreach. It is a public-data handoff shape an endpoint owner can publish, attach to an issue, or adapt after a real request.

## When To Use It

Good trigger:

- `developer_tool_hit`, `agent_crawler_hit`, MCP manifest fetches, or `x402_probe` increased
- HTTP `402` responses increased while paid calls stayed at zero
- durable product totals increased or stayed healthy
- `paid_calls=0`
- `readiness_subscription_intent=0`
- `alert_subscriptions=0`
- `third_party_submission=0`

Do not use it to imply customer demand. Machine inspection is attention, not revenue.

## Handoff

```text
Subject: MCP/x402 probe handoff for <endpoint name>

Public endpoint:
MCP endpoint:
x402 manifest:
Latest durable totals:
Latest probe window:
Buyer-action boundary:

What changed:
Developer tools, crawlers, or x402 probes inspected the endpoint, but no paid call, subscription intent, listing submission, or buyer reply followed.

Current interpretation:
The endpoint is discoverable enough to be inspected. The next buyer-safe action is still unclear.

Probe-to-payment interpretation:
If `x402_probe` or HTTP `402` responses increased but `paid_calls=0`, payment-aware clients reached the paid boundary and stopped. The handoff should make the cheapest paid action, free preflight, quote/audit evidence, and stop conditions obvious.

Recommended public next step:
Publish or attach one short readiness note that answers:

1. What can an agent call safely?
2. What does each paid action cost, on which chain and currency?
3. What happens before a mutating or paid action runs?
4. What receipt or response proves the call completed?
5. What should a directory, buyer, or endpoint owner do next?
6. What is the cheapest safe paid probe, and what does it return?

Boundary:
Public evidence only. No private analytics, secrets, wallet keys, outreach, payment-link changes, legal/security certification, or guaranteed listing/revenue claim.
```

## Fit-Check Issue Snapshot

Paste this into the MCP/x402 audit request issue when the signal is real but still pre-revenue:

```text
Endpoint:
MCP manifest:
x402 manifest:
Latest durable totals: total_reports=<n>, ready_reports=<n>
Latest probe window: developer_tool_hit=<n>, agent_crawler_hit=<n>, x402_probe=<n>, http_402_responses=<n>
Buyer-action boundary: paid_calls=0, settle_successes=0, readiness_subscription_intent=0, alert_subscriptions=0, third_party_submission=0
Desired outcome: one public probe-to-payment handoff before outreach, listing repair, or payment-path changes
```

## Stop Conditions

Stop and ask for owner approval before:

- contacting a directory, maintainer, buyer, or third party
- submitting or editing an external listing
- creating accounts
- changing payment links or collection flows
- deploying production code
- claiming revenue or buyer interest

The useful result is a sharper public next action, not a louder claim.
