import requests
from base64 import b64decode

GITHUB_USERNAME = "PrajwalDataScientist"
REPO_NAME = "prajwal_ai_assistant"

def fetch_github_project():
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.get(url)
    if response.status_code == 200:
        repo = response.json()
        return {
            "name": repo["name"],
            "description": repo["description"] or "No description provided.",
            "url": repo["html_url"]
        }
    else:
        return f"Error fetching repository: {response.status_code}"

def fetch_readme():
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/readme"
    response = requests.get(url)
    if response.status_code == 200:
        readme_content = response.json()["content"]
        decoded = b64decode(readme_content).decode("utf-8")
        return decoded
    else:
        return f"README not available. Error: {response.status_code}"

# Example usage:
print(fetch_github_project())
print(fetch_readme())
