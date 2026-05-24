from exceptions import GithubClientError, GithubConnectionError, GithubNotFoundError
import requests
from typing import Dict, List, Any

def get_recent_github_issues(owner: str, repo: str, limit: int = 10, is_open: bool = True) -> List[Dict[str, Any]]:
    
    base_url = "https://api.github.com/search/issues"

    state = "open" if is_open else "closed"
    
    query = f"repo:{owner}/{repo} is:issue is:{state}"
    
    params = {
        "q": query,
        "sort": "created",
        "order": "desc",
        "per_page": limit
    }

    try:
        response = requests.get(base_url, params=params, timeout=10.0)
        response.raise_for_status()
        
        return response.json().get("items", [])


    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise GithubNotFoundError(f"repo not found: {owner}/{repo}") from e
        raise GithubClientError(f"api error: {e.response.status_code}") from e
        
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        raise GithubConnectionError("connection failed") from e
        
    except requests.exceptions.RequestException as e:
        raise GithubClientError("unexpected request error") from e
        
    except ValueError as e:
        raise GithubClientError("invalid json response") from e