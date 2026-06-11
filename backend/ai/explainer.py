from backend.ai.gemini_client import client


def generate_remediation(finding):

    prompt = f"""
You are a Senior DevOps, SRE and Platform Engineer.

Finding Rule:
{finding["rule"]}

Finding Message:
{finding["message"]}

Explain:

1. Why this issue matters.
2. Risks if ignored.
3. Recommended fix.
4. Best practice.

Keep the response under 200 words.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text