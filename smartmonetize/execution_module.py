"""Local execution helpers for SmartMonetize recommendations."""

from __future__ import annotations

from .data_collection import ProductMetrics
from .strategy_analysis import RevenueMove


def render_markdown_report(metrics: ProductMetrics, moves: list[RevenueMove]) -> str:
    lines = [
        f"# SmartMonetize Audit: {metrics.product}",
        "",
        "## Snapshot",
        "",
        f"- Monthly visitors: `{metrics.monthly_visitors}`",
        f"- Qualified clicks: `{metrics.qualified_clicks}`",
        f"- Signups: `{metrics.signups}`",
        f"- Paid customers: `{metrics.paid_customers}`",
        f"- Average price: `${metrics.average_price_usd:.2f}`",
        f"- Clear offer: `{str(metrics.has_clear_offer).lower()}`",
        f"- Checkout path: `{str(metrics.has_checkout).lower()}`",
        f"- Analytics: `{str(metrics.has_analytics).lower()}`",
        "",
        "## Ranked Moves",
        "",
    ]
    for index, move in enumerate(moves, 1):
        lines.extend(
            [
                f"### {index}. {move.title}",
                "",
                move.why,
                "",
                f"- Priority score: `{move.priority:.2f}`",
                f"- Expected revenue: `${move.expected_revenue_usd:.2f}`",
                f"- Owner time: `{move.owner_minutes_required} min`",
                f"- External action required: `{str(move.external_action_required).lower()}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Boundary",
            "",
            "This report does not send messages, publish changes, create accounts, spend money, or alter payment systems.",
        ]
    )
    return "\n".join(lines).strip() + "\n"
