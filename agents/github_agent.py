from github_handler.github_api import fetch_github_projects as get_github_projects

def fetch_github_projects():
    repos = get_github_projects()
    return repos
