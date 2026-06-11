def check_privileged_container(resource):

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

        security_context = container.get(
            "securityContext",
            {}
        )

        if security_context.get("privileged") is True:

            findings.append({
                "severity": "CRITICAL",
                "rule": "PRIVILEGED_CONTAINER",
                "container": container.get("name"),
                "message": "Privileged container detected"
            })

    return findings

def check_root_user(resource):

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

        security_context = container.get(
            "securityContext",
            {}
        )

        if security_context.get("runAsUser") == 0:

            findings.append({
                "severity": "HIGH",
                "rule": "RUNNING_AS_ROOT",
                "container": container.get("name"),
                "message": "Container running as root user"
            })

    return findings

def check_missing_security_context(resource):

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

        if "securityContext" not in container:

            findings.append({
                "severity": "MEDIUM",
                "rule": "MISSING_SECURITY_CONTEXT",
                "container": container.get("name"),
                "message": "Container missing securityContext"
            })

    return findings

def check_latest_tag(resource):

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

        image = container.get("image", "")

        if image.endswith(":latest"):

            findings.append({
                "severity": "MEDIUM",
                "rule": "LATEST_IMAGE_TAG",
                "container": container.get("name"),
                "message": "Container using latest image tag"
            })

    return findings

def check_cluster_admin(resource):

    findings = []

    if resource.get("kind") != "ClusterRoleBinding":
        return findings

    role_ref = resource.get("roleRef", {})

    if role_ref.get("name") == "cluster-admin":

        findings.append({
            "severity": "CRITICAL",
            "rule": "CLUSTER_ADMIN_BINDING",
            "message": "Cluster admin role assigned"
        })

    return findings