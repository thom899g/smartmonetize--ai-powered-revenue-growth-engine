"""SmartMonetize: deterministic revenue triage for small products."""

from .data_collection import ProductMetrics, load_metrics, metrics_from_dict
from .strategy_analysis import RevenueMove, recommend_moves, summarize

__all__ = [
    "ProductMetrics",
    "RevenueMove",
    "load_metrics",
    "metrics_from_dict",
    "recommend_moves",
    "summarize",
]
