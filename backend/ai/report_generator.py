from backend.ai.gemini_client import client


def generate_ai_report(findings, score):

    findings_text = ""

    for idx, finding in enumerate(findings, start=1):

        findings_text += f"""
Finding {idx}

Rule: {finding['rule']}
Severity: {finding['severity']}
Message: {finding['message']}

"""

    prompt = f"""
You are a Principal Platform Engineer.

Analyze the following Kubernetes and Terraform findings.

Security Score:
{score}/100

Findings:

{findings_text}

Generate a report with:

1. Executive Summary
2. Critical Risks
3. Reliability Risks
4. Security Risks
5. Recommended Actions (priority order)
6. Overall Assessment

Keep response under 500 words & use the exact format as shown for the report.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text