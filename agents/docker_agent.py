from github_handler.docker_api import fetch_docker_repos as get_docker_repos

def fetch_docker_repos():
    repos = get_docker_repos()
    return repos
