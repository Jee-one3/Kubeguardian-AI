from backend.knowledge.rule_knowledge import (
    RULE_KNOWLEDGE
)


def enrich_findings(findings):

    enriched = []

    for finding in findings:

        rule = finding["rule"]

        knowledge = RULE_KNOWLEDGE.get(
            rule,
            {}
        )

        finding["risk"] = knowledge.get(
            "risk",
            "Unknown"
        )

        finding["impact"] = knowledge.get(
            "impact",
            "Unknown"
        )

        finding["recommended_fix"] = knowledge.get(
            "fix",
            "Review manually"
        )

        finding["priority"] = knowledge.get(
            "priority",
            "P4"
        )

        enriched.append(
            finding
        )

    return enriched