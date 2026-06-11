from backend.rules.terraform_rules import (
    check_missing_tags,
    check_hardcoded_instance_types,
    check_open_security_groups,
    check_missing_backend
)


def analyze_terraform(terraform_data):

    findings = []

    findings.extend(
        check_missing_tags(terraform_data)
    )

    findings.extend(
        check_hardcoded_instance_types(terraform_data)
    )

    findings.extend(
        check_open_security_groups(terraform_data)
    )

    findings.extend(
        check_missing_backend(terraform_data)
    )

    score = 100

    for finding in findings:

        severity = finding["severity"]

        if severity == "CRITICAL":
            score -= 20

        elif severity == "HIGH":
            score -= 15

        elif severity == "MEDIUM":
            score -= 10

        elif severity == "LOW":
            score -= 5

    score = max(score, 0)

    return {
        "score": score,
        "findings": findings
    }