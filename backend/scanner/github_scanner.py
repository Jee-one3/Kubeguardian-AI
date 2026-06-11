import shutil
import os

from git import Repo


CLONE_DIR = "repos"


def clone_repository(repo_url):

    os.makedirs(
        CLONE_DIR,
        exist_ok=True
    )

    repo_name = (
        repo_url.split("/")[-1]
        .replace(".git", "")
    )

    repo_path = os.path.join(
        CLONE_DIR,
        repo_name
    )

    if os.path.exists(repo_path):

        shutil.rmtree(repo_path)

    Repo.clone_from(
        repo_url,
        repo_path
    )

    return repo_path