
import requests

BASE_URL = "https://api.github.com"


def github_profile(username):
    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(
        f"{BASE_URL}/users/{username}",
        headers=headers,
        timeout=10
    )
    response.raise_for_status()
    user = response.json()

    response = requests.get(
        f"{BASE_URL}/users/{username}/repos",
        params={"per_page": 10, "sort": "updated"},
        headers=headers,
        timeout=10
    )
    response.raise_for_status()
    repos = response.json()

    languages = {}

    for repo in repos:
        language = repo.get("language")
        if language:
            languages[language] = languages.get(language, 0) + 1

    return {
        "username": user.get("login"),
        "name": user.get("name"),
        "bio": user.get("bio"),
        "company": user.get("company"),
        "location": user.get("location"),
        "public_repos": user.get("public_repos"),
        "top_languages_in_recent_repos": languages,
        "recent_public_repositories": [
            {
                "name": repo.get("name"),
                "language": repo.get("language"),
                "description": repo.get("description"),
                "url": repo.get("html_url")
            }
            for repo in repos
        ]
    }
