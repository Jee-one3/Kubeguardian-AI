import os


def discover_files(repo_path):

    terraform_files = []

    kubernetes_files = []

    for root, dirs, files in os.walk(
        repo_path
    ):

        for file in files:

            full_path = os.path.join(
                root,
                file
            )

            if file.endswith(".tf"):

                terraform_files.append(
                    full_path
                )

            elif file.endswith(".yaml") \
            or file.endswith(".yml"):

                kubernetes_files.append(
                    full_path
                )

    return {
        "terraform": terraform_files,
        "kubernetes": kubernetes_files
    }