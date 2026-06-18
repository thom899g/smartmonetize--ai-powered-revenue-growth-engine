"""Deterministic revenue strategy scoring."""

from __future__ import annotations

from dataclasses import dataclass

from .data_collection import ProductMetrics


@dataclass(frozen=True)
class RevenueMove:
    title: str
    why: str
    expected_revenue_usd: float
    probability: float
    repeatability: float
    setup_hours: float
    owner_minutes_required: int
    risk_penalty: float
    external_action_required: bool

    @property
    def priority(self) -> float:
        hourly_cost = 50.0
        owner_effort_penalty = (self.owner_minutes_required / 60.0) * hourly_cost
        raw_score = (
            self.expected_revenue_usd * self.probability * self.repeatability
            - self.setup_hours * hourly_cost
            - owner_effort_penalty
            - self.risk_penalty
        )
        return round(raw_score + 100.0, 2)


def _traffic_quality(metrics: ProductMetrics) -> str:
    if metrics.qualified_clicks >= 50 or metrics.signups >= 5:
        return "meaningful"
    if metrics.qualified_clicks > 0 or metrics.monthly_visitors >= 100:
        return "early"
    return "missing"


def recommend_moves(metrics: ProductMetrics) -> list[RevenueMove]:
    moves: list[RevenueMove] = []
    price = metrics.average_price_usd or 49.0
    traffic = _traffic_quality(metrics)

    if traffic in {"early", "meaningful"} and metrics.paid_customers == 0:
        moves.append(
            RevenueMove(
                title="Add a direct paid pilot CTA",
                why="There is attention but no paid conversion. A concrete pilot offer is the fastest test.",
                expected_revenue_usd=max(price, 49.0),
                probability=0.22 if traffic == "meaningful" else 0.12,
                repeatability=0.8,
                setup_hours=0.5,
                owner_minutes_required=20,
                risk_penalty=5,
                external_action_required=False,
            )
        )

    if not metrics.has_clear_offer:
        moves.append(
            RevenueMove(
                title="Rewrite the offer around one buyer and one paid outcome",
                why="Traffic cannot convert if the buyer cannot quickly see what they get and why they should pay.",
                expected_revenue_usd=max(price, 49.0),
                probability=0.18,
                repeatability=0.9,
                setup_hours=0.75,
                owner_minutes_required=10,
                risk_penalty=2,
                external_action_required=False,
            )
        )

    if not metrics.has_checkout and metrics.signups > 0:
        moves.append(
            RevenueMove(
                title="Prepare an owner-approved payment path",
                why="Signups without a safe payment path leave revenue uncaptured.",
                expected_revenue_usd=max(price * max(metrics.signups, 1), price),
                probability=0.15,
                repeatability=0.75,
                setup_hours=1.0,
                owner_minutes_required=25,
                risk_penalty=12,
                external_action_required=True,
            )
        )

    if not metrics.has_analytics:
        moves.append(
            RevenueMove(
                title="Add one conversion measurement point",
                why="Without a basic signal, weak channels cannot be killed and strong channels cannot be scaled.",
                expected_revenue_usd=max(price, 49.0),
                probability=0.08,
                repeatability=0.7,
                setup_hours=0.5,
                owner_minutes_required=10,
                risk_penalty=1,
                external_action_required=False,
            )
        )

    if metrics.owner_minutes_available <= 15:
        moves.append(
            RevenueMove(
                title="Create a one-click owner decision packet",
                why="The owner has little time. Reduce the next revenue action to approve, edit, or reject.",
                expected_revenue_usd=max(price, 49.0),
                probability=0.1,
                repeatability=0.85,
                setup_hours=0.4,
                owner_minutes_required=5,
                risk_penalty=1,
                external_action_required=False,
            )
        )

    return sorted(moves, key=lambda item: item.priority, reverse=True)


def summarize(metrics: ProductMetrics) -> dict:
    moves = recommend_moves(metrics)
    top = moves[0] if moves else None
    return {
        "product": metrics.product,
        "traffic_quality": _traffic_quality(metrics),
        "conversion_rates": {
            "visitor_to_click": metrics.visitor_to_click_rate,
            "click_to_signup": metrics.signup_rate,
            "signup_to_paid": metrics.paid_conversion_rate,
        },
        "top_move": top.title if top else "Collect a real market signal",
        "moves": [
            {
                "title": move.title,
                "why": move.why,
                "priority": round(move.priority, 2),
                "expected_revenue_usd": move.expected_revenue_usd,
                "owner_minutes_required": move.owner_minutes_required,
                "external_action_required": move.external_action_required,
            }
            for move in moves
        ],
    }
