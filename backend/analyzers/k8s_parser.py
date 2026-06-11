import yaml


def load_kubernetes_manifest(file_path):
    """
    Load one or more Kubernetes resources
    from a YAML file.
    """

    with open(file_path, "r") as file:
        documents = list(yaml.safe_load_all(file))

    return documents