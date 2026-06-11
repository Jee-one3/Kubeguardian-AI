def check_single_replica(resource):

    findings = []

    if resource.get("kind") != "Deployment":
        return findings

    replicas = (
        resource.get("spec", {})
        .get("replicas", 1)
    )

    if replicas < 2:
        findings.append({
            "severity": "MEDIUM",
            "rule": "SINGLE_REPLICA",
            "message": "Deployment has only one replica"
        })

    return findings


def check_liveness_probe(resource):

    findings = []

    if resource.get("kind") != "Deployment":
        return findings

    containers = (
        resource.get("spec", {})
        .get("template", {})
        .get("spec", {})
        .get("containers", [])
    )

    for container in containers:

        if "livenessProbe" not in container:

            findings.append({
                "severity": "HIGH",
                "rule": "MISSING_LIVENESS_PROBE",
                "container": container.get("name"),
                "message": "Container missing liveness probe"
            })

    return findings


def check_readiness_probe(resource):

    findings = []

    if resource.get("kind") != "Deployment":
        return findings

    containers = (
        resource.get("spec", {})
        .get("template", {})
        .get("spec", {})
        .get("containers", [])
    )

    for container in containers:

        if "readinessProbe" not in container:

            findings.append({
                "severity": "HIGH",
                "rule": "MISSING_READINESS_PROBE",
                "container": container.get("name"),
                "message": "Container missing readiness probe"
            })

    return findings


def check_resource_requests(resource):

    findings = []

    if resource.get("kind") != "Deployment":
        return findings

    containers = (
        resource.get("spec", {})
        .get("template", {})
        .get("spec", {})
        .get("containers", [])
    )

    for container in containers:

        resources = container.get("resources", {})

        requests = resources.get("requests")

        if not requests:

            findings.append({
                "severity": "MEDIUM",
                "rule": "MISSING_RESOURCE_REQUESTS",
                "container": container.get("name"),
                "message": "Container missing resource requests"
            })

    return findings


def check_resource_limits(resource):

    findings = []

    if resource.get("kind") != "Deployment":
        return findings

    containers = (
        resource.get("spec", {})
        .get("template", {})
        .get("spec", {})
        .get("containers", [])
    )

    for container in containers:

        resources = container.get("resources", {})

        limits = resources.get("limits")

        if not limits:

            findings.append({
                "severity": "MEDIUM",
                "rule": "MISSING_RESOURCE_LIMITS",
                "container": container.get("name"),
                "message": "Container missing resource limits"
            })

    return findings