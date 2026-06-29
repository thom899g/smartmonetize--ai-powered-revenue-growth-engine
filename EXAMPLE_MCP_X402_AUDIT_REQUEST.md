# Example MCP/x402 Audit Request

Use this shape when your public endpoint has crawler, directory, repo, or tool attention but no buyer action yet.

Do not include passwords, API keys, wallet secrets, payment details, private customer data, confidential contracts, or private admin URLs.

## Public Fit-Check Issue

```text
Product or endpoint name:
Example MCP/x402 Service

Public endpoint URL:
https://example.com/mcp

x402 manifest URL:
https://example.com/.well-known/x402.json

MCP manifest URL:
https://example.com/.well-known/mcp.json

Current public market signal:
durable totals: total_reports=3240, ready_reports=3069
latest window: developer_tool_hit=3, agent_crawler_hit=1, x402_probe=0, human_visit=0, paid_calls=0
prior window if known: total_reports=3234, ready_reports=3063, developer_tool_hit=1, x402_probe=8, agent_crawler_hit=0, human_visit=0
repo_stars=1

Where did the attention come from?
awesome-x402 listing, third-party directory page, public visits, MCP manifest fetches, public repo activity, and x402 probe counter.

Directory page if applicable:
https://agent-tools.cloud/services/ontario-protocol-ontarioprotocol-com-x402

Directory status:
accepted awesome-x402 listing; live agent-tools row is public but shows `conformance: fail`; live agent-buyer guide URL currently returns 404 while MCP and x402 manifests are reachable

Current conversion boundary:
paid_calls=0
readiness_subscription_intent=0
alert_subscriptions=0
third_party_submission=0
buyer replies=0

Desired outcome:
One buyer-safe next action that can turn machine discovery into an endpoint-owner inquiry, live agent-buyer guide fix, paid call, subscription intent, or readiness proof.

Constraints:
Public data only. No outreach, ads, payment-provider changes, private analytics, or admin access.

Are you interested in the $199 paid pilot if the fit is clear?
Maybe, show me the free public fit check first.
```

## Why This Is Enough

The audit starts from the boundary between attention and buyer action. It needs one public endpoint, one public signal snapshot, and one conversion gap.

Separate durable totals from counters that may reset between deploys, days, or storage restores. For example, growing report totals plus a smaller latest-window `x402_probe` or `developer_tool_hit` count is valid attention for a free fit check, but reset-prone drops are not negative buyer evidence by themselves.

The most useful signals are concrete counts or public URLs:

- directory listing or crawler fetch
- repo star, fork, issue, or release reaction
- tool or probe counter
- public report count
- signup, paid call, subscription intent, payment discussion, or payment
- latest-window counters plus prior-window counters when a reset may have happened

The most useful boundary is also concrete:

- `paid_calls=0`
- `subscription_intent=0`
- `buyer replies=0`
- `accepted listings=0`
- `payment discussion=0`

The output is not a revenue promise. It is one small endpoint-owner action plan with a follow-up measurement window.
