import requests

DOCKER_USERNAME = "prajwal1027"  # Replace with your DockerHub username

def fetch_docker_repos():
    url = f"https://hub.docker.com/v2/repositories/{DOCKER_USERNAME}/"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()['results']
        repo_list = []
        for repo in repos:
            repo_list.append({
                "name": repo["name"],
                "description": repo.get("description", "No description provided."),
                "pulls": repo["pull_count"],
                "stars": repo["star_count"],
                "url": f"https://hub.docker.com/r/{DOCKER_USERNAME}/{repo['name']}"
            })
        return repo_list
    else:
        return f"Error fetching DockerHub repositories: {response.status_code}"
