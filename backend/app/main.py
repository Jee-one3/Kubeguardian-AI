from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
import os
from backend.knowledge.enricher import (
    enrich_findings
)
from backend.analyzers.k8s_parser import load_kubernetes_manifest
from backend.analyzers.k8s_analyzer import analyze_resources

from backend.analyzers.terraform_parser import (
    load_terraform_file
)

from backend.analyzers.terraform_analyzer import (
    analyze_terraform
)
from backend.reports.summary_builder import (
    build_summary
)

from backend.ai.executive_summary import (
    generate_executive_summary
)

from backend.ai.remediation_report import (
    generate_remediation_report
)
from backend.reports.pdf_generator import (
    generate_pdf_report
)

from backend.model.github_request import (
    GithubRequest
)

from backend.scanner.github_scanner import (
    clone_repository
)

from backend.scanner.file_discovery import (
    discover_files
)

from backend.scanner.repository_analyzer import (
    analyze_terraform_files
)

app = FastAPI(
    title="KubeGuardian AI"
)

UPLOAD_DIR = "backend/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {"message": "KubeGuardian AI Running"}


@app.post("/analyze")
async def analyze_yaml(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    if file.filename.endswith(".yaml") \
    or file.filename.endswith(".yml"):

        resources = load_kubernetes_manifest(file_path)

        analysis = analyze_resources(resources)
        analysis["findings"] = enrich_findings(
            analysis["findings"]
        )

    elif file.filename.endswith(".tf"):

        terraform_data = load_terraform_file(
            file_path
        )

        analysis = analyze_terraform(
            terraform_data
        )
        analysis["findings"] = enrich_findings(
            analysis["findings"]
        )
    else:

        return {
            "error": "Unsupported file type"
        }

    summary = build_summary(
        analysis["findings"]
    )

    executive_summary = (
        generate_executive_summary(
            analysis["score"],
            summary
        )
    )

    remediation_report = (
        generate_remediation_report(
        analysis["findings"]
        )
    ) 
    pdf_report = generate_pdf_report(
        analysis,
        summary,
        executive_summary,
        remediation_report
    )  
    return {

        "status": "success",

        "summary": summary,

        "analysis": analysis,

        "executive_summary": executive_summary,

        "remediation_report": remediation_report,

        "pdf_report": pdf_report
    }
@app.post(
    "/analyze-repository"
)
def analyze_repository(
    request: GithubRequest
):

    repo_path = clone_repository(
        request.repo_url
    )

    files = discover_files(
        repo_path
    )

    analysis = (
        analyze_terraform_files(
            files["terraform"]
        )
    )

    return {
        "repository":
        request.repo_url,

        "terraform_files":
        len(
            files["terraform"]
        ),

        "analysis":
        analysis
    }