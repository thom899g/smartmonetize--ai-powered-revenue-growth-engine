from smartmonetize.data_collection import metrics_from_dict
from smartmonetize.execution_module import render_markdown_report
from smartmonetize.strategy_analysis import recommend_moves, summarize


def test_recommends_paid_cta_for_attention_without_revenue():
    metrics = metrics_from_dict(
        {
            "product": "Test Product",
            "monthly_visitors": 1000,
            "qualified_clicks": 80,
            "signups": 4,
            "paid_customers": 0,
            "average_price_usd": 99,
            "has_clear_offer": True,
            "has_checkout": False,
            "has_analytics": True,
        }
    )

    moves = recommend_moves(metrics)

    assert moves
    assert moves[0].title == "Add a direct paid pilot CTA"
    assert moves[0].external_action_required is False


def test_summary_contains_ranked_moves():
    metrics = metrics_from_dict({"product": "Noisy Prototype", "monthly_visitors": 250})

    summary = summarize(metrics)

    assert summary["product"] == "Noisy Prototype"
    assert summary["moves"]
    assert "priority" in summary["moves"][0]


def test_markdown_report_states_boundary():
    metrics = metrics_from_dict({"product": "Boundary Test", "monthly_visitors": 250})
    report = render_markdown_report(metrics, recommend_moves(metrics))

    assert "does not send messages" in report
    assert "Ranked Moves" in report
