from github_client import get_recent_github_issues
from issues_parser import parse_github_issues
from claude_client import send_claude_request
from prompts import OPEN_ISSUES_SYSTEM_PROMPT, CLOSED_ISSUES_SYSTEM_PROMPT

def process_open_issues() -> str:
    raw_issues = get_recent_github_issues(is_open=True)
    parsed_issues = parse_github_issues(raw_issues)
    
    return send_claude_request(
        prompt=str(parsed_issues),
        system_prompt=OPEN_ISSUES_SYSTEM_PROMPT
    )

def process_closed_issues() -> str:
    raw_issues = get_recent_github_issues(is_open=False)
    parsed_issues = parse_github_issues(raw_issues)
    
    return send_claude_request(
        prompt=str(parsed_issues),
        system_prompt=CLOSED_ISSUES_SYSTEM_PROMPT
    )