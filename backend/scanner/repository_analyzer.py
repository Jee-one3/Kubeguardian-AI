from backend.analyzers.terraform_parser import (
    load_terraform_file
)

from backend.analyzers.terraform_analyzer import (
    analyze_terraform
)


def analyze_terraform_files(
    terraform_files
):

    findings = []

    lowest_score = 100

    for file_path in terraform_files:

        try:

            data = load_terraform_file(
                file_path
            )

            result = analyze_terraform(
                data
            )

            findings.extend(
                result["findings"]
            )

            lowest_score = min(
                lowest_score,
                result["score"]
            )

        except Exception as e:

            print(
                f"Failed: {file_path}"
            )

    return {
        "score": lowest_score,
        "findings": findings
    }