import requests
from base64 import b64decode

# You can move this to a config file later
GITHUB_USERNAME = "PrajwalDataAnalyst"
GITHUB_API_URL = f"https://api.github.com/PrajwalDataScientist/prajwal_ai_assistant"

def fetch_github_projects():
    """
    Fetches all public repositories for the configured GitHub user.
    """
    response = requests.get(GITHUB_API_URL)
    if response.status_code == 200:
        repos = response.json()
        repo_list = []
        for repo in repos:
            repo_list.append({
                "name": repo["name"],
                "description": repo["description"] or "No description provided.",
                "url": repo["html_url"]
            })
        return repo_list
    else:
        return f"Error fetching repositories: {response.status_code}"

def fetch_readme(repo_name):
    """
    Fetches the README content for a specific repository.
    """
    url = f"https://api.github.com/repos/{prajwal_ai_assistant}/{repo_name}/readme"
    response = requests.get(url)
    if response.status_code == 200:
        readme_content = response.json()["content"]
        decoded_content = b64decode(readme_content).decode('utf-8')
        return decoded_content
    else:
        return "README not available for this repository."
