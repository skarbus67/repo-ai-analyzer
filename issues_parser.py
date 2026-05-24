from typing import Dict, List, Any


def parse_github_issues(raw_issues: List[Dict[str, Any]]) -> List[Dict[str, Any]]:

    parsed_issues = []
    
    for issue in raw_issues:
        body_text = issue.get("body")
        if not body_text:
            body_text = ""

            
        labels = [label.get("name") for label in issue.get("labels")]

        assignees = [assignee.get("login") for assignee in (issue.get("assignees") or [])]

        parsed_issue = {
            "id": issue.get("number"),
            "title": issue.get("title"),
            "body": body_text,
            "state": issue.get("state"),
            "created_at": issue.get("created_at"),
            "author": issue.get("user").get("login"),
            "labels": labels,
            "assignees": assignees
        }
        
        parsed_issues.append(parsed_issue)
        
    return parsed_issues