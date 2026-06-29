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
    mcp_template = Path(".github/ISSUE_TEMPLATE/mcp_x402_endpoint_audit.yml").read_text(
        encoding="utf-8"
    )
    agent_template = Path(".github/ISSUE_TEMPLATE/agent_mcp_trust_boundary_audit.yml").read_text(
        encoding="utf-8"
    )

    assert "package_type" in template
    assert "MCP/x402 Endpoint Mini-Audit - $199 pilot" in template
    assert "endpoint" in template
    assert "desired_outcome" in template
    assert "pilot_interest" in template
    assert "Do not include passwords" in template
    assert "revenue-audit" in template
    assert "MCP/x402 Endpoint Mini-Audit Request" in mcp_template
    assert "mcp-x402" in mcp_template
    assert "x402_manifest" in mcp_template
    assert "mcp_manifest" in mcp_template
    assert "current_signal" in mcp_template
    assert "paid_calls=0" in mcp_template
    assert "reset-prone counters" in mcp_template
    assert "Do not include passwords" in mcp_template
    assert "Agent/MCP Trust Boundary Audit Request" in agent_template
    assert "$299" in agent_template
    assert "public_url" in agent_template
    assert "capabilities" in agent_template
    assert "conversion_boundary" in agent_template
    assert "Do not include passwords" in agent_template


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
    trust_boundary_audit = Path("AGENT_MCP_TRUST_BOUNDARY_AUDIT.md").read_text(
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
    assert "Found This From `x402-service`, `mcp-server`, Or `agent-commerce`?" in readme
    assert "Revenue Triage Audit Request" in readme
    assert "MCP/x402 Endpoint Mini-Audit Request" in readme
    assert "mcp_x402_endpoint_audit.yml" in readme
    assert "free public fit-check issue" in readme
    assert "Do not include passwords" in readme
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
    assert "AGENT_MCP_TRUST_BOUNDARY_AUDIT.md" in readme
    assert "Agent/MCP Trust Boundary Audit request issue form" in readme
    assert "MCP_X402_ENDPOINT_AUDIT.md" in offer
    assert "AGENT_MCP_TRUST_BOUNDARY_AUDIT.md" in offer
    assert "MCP_X402_ENDPOINT_AUDIT.md" in quickstart
    assert "FIRST_RESPONSE_MCP_X402_AUDIT_SKELETON.md" in readme
    assert "FIRST_RESPONSE_MCP_X402_AUDIT_SKELETON.md" in mcp_x402_audit
    first_response = Path("FIRST_RESPONSE_MCP_X402_AUDIT_SKELETON.md").read_text(
        encoding="utf-8"
    )
    assert "public-data response skeleton" in first_response
    assert "Only discuss the `$199` MCP/x402 Endpoint Mini-Audit" in first_response
    assert "No guarantee of listing acceptance" in first_response
    assert "MCP/x402 Endpoint Mini-Audit" in release_notes
    assert "Agent/MCP Trust Boundary Audit" in release_notes
    assert "$299" in trust_boundary_audit
    assert "trust-boundary map" in trust_boundary_audit
    assert "No guarantee" in trust_boundary_audit
    assert "passwords" in trust_boundary_audit
    assert "agent_mcp_trust_boundary_audit.yml" in readme
    assert "McpX402Audit" in pyproject
    assert "AgentMcpTrustAudit" in pyproject
    assert "McpX402AuditRequest" in pyproject
    assert "$199" in mcp_x402_audit
    assert "No guarantee" in mcp_x402_audit or "no guarantee" in mcp_x402_audit
    assert "passwords" in mcp_x402_audit
    assert "durable totals" in mcp_x402_audit
    assert "MCP/x402 Endpoint Mini-Audit Request" in mcp_x402_audit
    assert "latest-window counters" in Path(
        "EXAMPLE_MCP_X402_AUDIT_REQUEST.md"
    ).read_text(encoding="utf-8")
    assert "free public fit check first" in Path(
        ".github/ISSUE_TEMPLATE/revenue_triage_audit.yml"
    ).read_text(encoding="utf-8")
