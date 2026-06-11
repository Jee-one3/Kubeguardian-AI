RULE_KNOWLEDGE = {

    "OPEN_SECURITY_GROUP": {
        "risk":
        "Public internet exposure",

        "impact":
        "Attackers can directly access workloads exposed through this security group.",

        "fix":
        "Restrict ingress CIDR ranges to trusted IP addresses.",

        "priority":
        "P1"
    },

    "MISSING_BACKEND": {
        "risk":
        "Terraform state inconsistency",

        "impact":
        "State corruption and infrastructure drift may occur.",

        "fix":
        "Configure remote backend using S3 or GCS.",

        "priority":
        "P1"
    },

    "MISSING_TAGS": {
        "risk":
        "Governance gaps",

        "impact":
        "Resource ownership and cost allocation become difficult.",

        "fix":
        "Apply mandatory tags such as Environment, Owner, Team.",

        "priority":
        "P3"
    },

    "HARDCODED_INSTANCE_TYPE": {
        "risk":
        "Reduced flexibility",

        "impact":
        "Scaling and instance upgrades require code modifications.",

        "fix":
        "Use Terraform variables for instance types.",

        "priority":
        "P4"
    },

    "MISSING_LIVENESS_PROBE": {
        "risk":
        "Undetected unhealthy containers",

        "impact":
        "Failed containers may continue running without restart.",

        "fix":
        "Configure liveness probes.",

        "priority":
        "P2"
    },

    "MISSING_READINESS_PROBE": {
        "risk":
        "Traffic routed to unhealthy pods",

        "impact":
        "Application downtime and failed deployments.",

        "fix":
        "Configure readiness probes.",

        "priority":
        "P2"
    },

    "MISSING_RESOURCE_LIMITS": {
        "risk":
        "Resource exhaustion",

        "impact":
        "Pods may consume excessive CPU or memory.",

        "fix":
        "Define resource limits.",

        "priority":
        "P2"
    },

    "MISSING_RESOURCE_REQUESTS": {
        "risk":
        "Poor scheduling",

        "impact":
        "Kubernetes scheduler cannot allocate resources efficiently.",

        "fix":
        "Define resource requests.",

        "priority":
        "P2"
    },

    "SINGLE_REPLICA": {
        "risk":
        "Single point of failure",

        "impact":
        "Pod failure can cause service outage.",

        "fix":
        "Run at least 2 replicas.",

        "priority":
        "P2"
    }
}