from backend.ai.gemini_client import client


def generate_remediation_report(findings):

    findings_text = ""

    for finding in findings:

        findings_text += f"""
Rule: {finding['rule']}
Severity: {finding['severity']}
Risk: {finding['risk']}
Impact: {finding['impact']}
Recommended Fix: {finding['recommended_fix']}
"""

    prompt = f"""
You are a Senior Platform Engineer.

Analyze these findings and generate:

1. Root Cause Analysis
2. Recommended Fixes
3. Priority Order (P1,P2,P3,P4)

Findings:

{findings_text}

Return concise markdown.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:

        return "AI remediation report unavailable."