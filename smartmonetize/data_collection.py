"""Input loading and normalization for SmartMonetize.

The collector is deliberately local-first. It reads metrics supplied by the
operator instead of scraping private dashboards or pretending to infer behavior
from arbitrary pages.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ProductMetrics:
    product: str
    monthly_visitors: int = 0
    qualified_clicks: int = 0
    signups: int = 0
    paid_customers: int = 0
    average_price_usd: float = 0.0
    has_clear_offer: bool = False
    has_checkout: bool = False
    has_analytics: bool = False
    owner_minutes_available: int = 30

    @property
    def visitor_to_click_rate(self) -> float:
        if self.monthly_visitors <= 0:
            return 0.0
        return self.qualified_clicks / self.monthly_visitors

    @property
    def signup_rate(self) -> float:
        if self.qualified_clicks <= 0:
            return 0.0
        return self.signups / self.qualified_clicks

    @property
    def paid_conversion_rate(self) -> float:
        if self.signups <= 0:
            return 0.0
        return self.paid_customers / self.signups


def _as_int(value: Any, default: int = 0) -> int:
    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return default


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        return max(0.0, float(value))
    except (TypeError, ValueError):
        return default


def _as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y", "on"}
    return bool(value)


def metrics_from_dict(data: dict[str, Any]) -> ProductMetrics:
    return ProductMetrics(
        product=str(data.get("product") or "Unnamed product").strip() or "Unnamed product",
        monthly_visitors=_as_int(data.get("monthly_visitors")),
        qualified_clicks=_as_int(data.get("qualified_clicks")),
        signups=_as_int(data.get("signups")),
        paid_customers=_as_int(data.get("paid_customers")),
        average_price_usd=_as_float(data.get("average_price_usd")),
        has_clear_offer=_as_bool(data.get("has_clear_offer")),
        has_checkout=_as_bool(data.get("has_checkout")),
        has_analytics=_as_bool(data.get("has_analytics")),
        owner_minutes_available=_as_int(data.get("owner_minutes_available"), 30),
    )


def load_metrics(path: str | Path) -> ProductMetrics:
    source = Path(path)
    data = json.loads(source.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("metrics file must contain a JSON object")
    return metrics_from_dict(data)
