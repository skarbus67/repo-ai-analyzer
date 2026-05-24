
class GithubClientError(Exception):
    pass

class GithubNotFoundError(GithubClientError):
    pass

class GithubConnectionError(GithubClientError):
    pass

class ClaudeClientError(Exception):
    pass

class ClaudeConnectionError(ClaudeClientError):
    pass