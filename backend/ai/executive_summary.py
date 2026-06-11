from backend.ai.gemini_client import client


def generate_executive_summary(
    score,
    summary
):

    prompt = f"""
You are KubeGuardian AI.

Security Score: {score}/100

Critical Findings: {summary['critical']}
High Findings: {summary['high']}
Medium Findings: {summary['medium']}
Low Findings: {summary['low']}

Generate an executive summary.

Maximum 150 words.

Do not mention specific rules.
Do not provide fixes.
Summarize overall platform health.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(f"Gemini Error: {e}")

        return (
            f"KubeGuardian detected "
            f"{summary['critical']} critical, "
            f"{summary['high']} high, "
            f"{summary['medium']} medium and "
            f"{summary['low']} low severity findings. "
            f"Overall platform score is "
            f"{score}/100."
        )