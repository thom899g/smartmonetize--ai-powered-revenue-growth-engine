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

    assert "package_type" in template
    assert "MCP/x402 Endpoint Mini-Audit - $199 pilot" in template
    assert "endpoint" in template
    assert "desired_outcome" in template
    assert "pilot_interest" in template
    assert "Do not include passwords" in template
    assert "revenue-audit" in template


def test_sample_report_shows_deliverable_and_boundaries():
    sample = Path("SAMPLE_REPORT.md").read_text(encoding="utf-8")
    readme = Path("README.md").read_text(encoding="utf-8")
    offer = Path("OFFER.md").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    release_notes = Path("RELEASE_NOTES.md").read_text(encoding="utf-8")
    quickstart = Path("QUICKSTART_TRIAGE.md").read_text(encoding="utf-8")
    case_study = Path("CASE_STUDY.md").read_text(encoding="utf-8")
    mcp_x402_audit = Path("MCP_X402_ENDPOINT_AUDIT.md").read_text(
        encoding="utf-8"
    )
    ontario_metrics = Path("examples/ontario_protocol_metrics.json").read_text(
        encoding="utf-8"
    )

    assert "SmartMonetize Sample Audit" in sample
    assert "Ranked Moves" in sample
    assert "7-Day Market Test" in sample
    assert "does not send messages" in sample
    assert "SAMPLE_REPORT.md" in readme
    assert "QUICKSTART_TRIAGE.md" in readme
    assert "SampleReport" in pyproject
    assert "AuditRequest" in pyproject
    assert "Audit request issue form" in release_notes
    assert "Ontario Protocol case study" in release_notes
    assert "Revenue Triage Audit Request" in quickstart
    assert "Do not include passwords" in quickstart
    assert "a star" in quickstart
    assert "CASE_STUDY.md" in readme
    assert "CASE_STUDY.md" in offer
    assert "CASE_STUDY.md" in quickstart
    assert "Ontario Protocol" in case_study
    assert "self-funded test payment" in case_study
    assert "Revenue Triage Audit Request" in case_study
    assert "Ontario Protocol" in ontario_metrics
    assert "MCP_X402_ENDPOINT_AUDIT.md" in readme
    assert "MCP_X402_ENDPOINT_AUDIT.md" in offer
    assert "MCP_X402_ENDPOINT_AUDIT.md" in quickstart
    assert "MCP/x402 Endpoint Mini-Audit" in release_notes
    assert "McpX402Audit" in pyproject
    assert "$199" in mcp_x402_audit
    assert "No guarantee" in mcp_x402_audit or "no guarantee" in mcp_x402_audit
    assert "passwords" in mcp_x402_audit
    assert "Revenue Triage Audit Request" in mcp_x402_audit
