from backend.analyzers.terraform_utils import clean_string
def check_missing_tags(terraform_data):

    findings = []

    resources = terraform_data.get("resource", [])

    for resource_block in resources:

        for resource_type, resource_values in resource_block.items():
            resource_type = clean_string(resource_type)

            for resource_name, config in resource_values.items():
                resource_name = clean_string(resource_name)
                if "tags" not in config:

                    findings.append({
                        "severity": "MEDIUM",
                        "rule": "MISSING_TAGS",
                        "resource_type": resource_type,
                        "resource_name": resource_name,
                        "message": "Resource missing tags"
                    })

    return findings

def check_hardcoded_instance_types(terraform_data):

    findings = []

    resources = terraform_data.get(
        "resource",
        []
    )

    for resource_block in resources:

        for resource_type, resource_values in resource_block.items():

            resource_type = clean_string(resource_type)

            if resource_type != "aws_instance":
                continue

            for resource_name, config in resource_values.items():

                resource_name = clean_string(
                    resource_name
                )

                if "instance_type" in config:

                    findings.append({
                        "severity": "LOW",
                        "rule": "HARDCODED_INSTANCE_TYPE",
                        "resource_type": resource_type,
                        "resource_name": resource_name,
                        "message": "Instance type is hardcoded"
                    })

    return findings

def check_open_security_groups(terraform_data):

    findings = []

    resources = terraform_data.get("resource", [])

    for resource_block in resources:

        for resource_type, resource_values in resource_block.items():

            resource_type = clean_string(resource_type)

            if resource_type != "aws_security_group":
                continue

            for resource_name, config in resource_values.items():

                resource_name = clean_string(resource_name)

                ingress_rules = config.get(
                    "ingress",
                    []
                )

                for ingress in ingress_rules:

                    cidrs = ingress.get(
                        "cidr_blocks",
                        []
                    )

                    cidrs = [
                        clean_string(c)
                        for c in cidrs
                    ]

                    if "0.0.0.0/0" in cidrs:

                        findings.append({
                            "severity": "CRITICAL",
                            "rule": "OPEN_SECURITY_GROUP",
                            "resource_type": resource_type,
                            "resource_name": resource_name,
                            "message": "Security group open to internet"
                        })

    return findings

def check_missing_backend(terraform_data):

    findings = []

    if "terraform" not in terraform_data:

        findings.append({
            "severity": "HIGH",
            "rule": "MISSING_BACKEND",
            "message": "Terraform backend not configured"
        })

    return findings