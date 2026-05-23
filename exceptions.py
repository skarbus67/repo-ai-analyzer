
class GithubClientError(Exception):
    pass

class GithubNotFoundError(GithubClientError):
    pass

class GithubConnectionError(GithubClientError):
    pass