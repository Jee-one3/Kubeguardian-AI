from pydantic import BaseModel


class GithubRequest(
    BaseModel
):
    repo_url: str