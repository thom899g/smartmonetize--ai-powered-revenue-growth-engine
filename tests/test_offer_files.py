from pathlib import Path


def test_offer_has_price_and_boundary():
    offer = Path("OFFER.md").read_text(encoding="utf-8")

    assert "$49" in offer
    assert "does not collect payment automatically" in offer
    assert "passwords" in offer


def test_issue_template_captures_buyer_interest_without_private_data():
    template = Path(".github/ISSUE_TEMPLATE/revenue_triage_audit.yml").read_text(
        encoding="utf-8"
    )

    assert "pilot_interest" in template
    assert "Do not include passwords" in template
    assert "revenue-audit" in template
