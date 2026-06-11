from backend.rules.reliability_rules import (
    check_single_replica,
    check_liveness_probe,
    check_readiness_probe,
    check_resource_requests,
    check_resource_limits
)

from backend.rules.security_rules import (
    check_privileged_container,
    check_root_user,
    check_missing_security_context,
    check_latest_tag,
    check_cluster_admin
)


def analyze_resources(resources):

    findings = []

    for resource in resources:

        if not resource:
            continue

        resource_name = (
            resource.get("metadata", {})
            .get("name")
        )

        findings.extend(
            check_single_replica(resource)
        )

        findings.extend(
            check_liveness_probe(resource)
        )

        findings.extend(
            check_readiness_probe(resource)
        )

        findings.extend(
            check_resource_requests(resource)
        )

        findings.extend(
            check_resource_limits(resource)
        )
        findings.extend(
            check_privileged_container(resource)
        )

        findings.extend(
            check_root_user(resource)
        )

        findings.extend(
            check_missing_security_context(resource)
        )

        findings.extend(
            check_latest_tag(resource)
        )

        findings.extend(
            check_cluster_admin(resource)
        )

        for finding in findings:
            finding["resource"] = resource_name
    for finding in findings:

        rule = finding["rule"]

        if rule in [
            "PRIVILEGED_CONTAINER",
            "RUNNING_AS_ROOT",
            "CLUSTER_ADMIN_BINDING",
            "LATEST_IMAGE_TAG",
            "MISSING_SECURITY_CONTEXT"
        ]:
            finding["category"] = "Security"

        else:
            finding["category"] = "Reliability"
    
    score = 100

    for finding in findings:
        severity = finding.get("severity")

    if severity == "CRITICAL":
        score -= 20

    elif severity == "HIGH":
        score -= 15

    elif severity == "MEDIUM":
        score -= 10

    elif severity == "LOW":
        score -= 5

    if score < 0:
        score = 0

    return {
    "score": score,
    "findings": findings
    }