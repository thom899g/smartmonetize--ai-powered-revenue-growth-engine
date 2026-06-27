# Directory Support Note Draft

Use this only after the endpoint owner approves contacting a directory or support inbox. It is not outreach copy to send automatically.

## When To Use

Use this draft when all of these are true:

- a public directory already lists the endpoint
- one directory row says `conformance: fail`, stale, incomplete, or missing metadata
- another row, MCP search result, or direct endpoint check says the service is live
- public counters show crawler, tool, x402 probe, or durable report movement
- buyer-action counters are still zero

Do not use it for cold outreach, mass submissions, private-data requests, payment collection, or legal/compliance claims.

## Evidence Packet

```text
Endpoint:
MCP URL:
x402 manifest:
Directory row with issue:
Directory row or endpoint check that passes:
Durable totals:
Latest-window counters:
Buyer-action boundary:
Owner-approved requested correction:
```

## Draft Note

```text
Subject: Ontario Protocol directory metadata appears stale across rows

Hi,

I own the endpoint below and noticed that the directory has mixed public results for the same service.

Endpoint:

MCP URL:

x402 manifest:

Current directory evidence:
- Row/result A:
- Row/result B:

Current public verification evidence:
- Direct endpoint status:
- Durable totals:
- Latest-window counters:

Buyer-action boundary:
- paid_calls=0
- readiness_subscription_intent=0
- alert_subscriptions=0
- third_party_submission=0

Could you re-check the endpoint metadata and let me know whether the failing row is stale or whether a specific field is still missing?

No private data is needed. I am looking for the smallest public metadata fix required for a consistent listing.
```

## Boundary

This note asks for a metadata re-check only. It must not claim accepted listing, buyer interest, revenue, certification, or third-party endorsement unless the directory has explicitly provided it.

## Success Signals

Scale only if one of these happens:

- directory row changes from fail/stale/incomplete to pass, ready, accepted, or equivalent
- directory replies with a concrete metadata blocker
- buyer or endpoint owner asks a specific follow-up question
- paid call, subscription intent, listing submission, or booked call appears

Revise if crawler or probe attention continues but buyer-action counters stay zero.

Kill if no new external signal appears after the approved watch window.
