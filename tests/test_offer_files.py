from pathlib import Path


def test_offer_has_price_and_boundary():
    offer = Path("OFFER.md").read_text(encoding="utf-8")

    assert "$49" in offer
    assert "does not collect payment automatically" in offer
    assert "passwords" in offer
    assert "Sample report" in offer


def test_issue_template_captures_buyer_interest_without_private_data():
    template = Path(".github/ISSUE_TEMPLATE/revenue_triage_audit.yml").read_text(
        encoding="utf-8"
    )

    assert "pilot_interest" in template
    assert "Do not include passwords" in template
    assert "revenue-audit" in template


def test_sample_report_shows_deliverable_and_boundaries():
    sample = Path("SAMPLE_REPORT.md").read_text(encoding="utf-8")
    readme = Path("README.md").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    release_notes = Path("RELEASE_NOTES.md").read_text(encoding="utf-8")

    assert "SmartMonetize Sample Audit" in sample
    assert "Ranked Moves" in sample
    assert "7-Day Market Test" in sample
    assert "does not send messages" in sample
    assert "SAMPLE_REPORT.md" in readme
    assert "SampleReport" in pyproject
    assert "AuditRequest" in pyproject
    assert "Audit request issue form" in release_notes
