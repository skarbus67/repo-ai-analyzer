import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not ANTHROPIC_API_KEY:
    raise ValueError("Missing ANTHROPIC_API_KEY in environment variables")

GITHUB_OWNER = os.getenv("GITHUB_OWNER")

if not GITHUB_OWNER:
    raise ValueError("Missing GITHUB_OWNER in environment variables")

GITHUB_REPO = os.getenv("GITHUB_REPO")

if not GITHUB_REPO:
    raise ValueError("Missing GITHUB_REPO in environment variables")

GITHUB_ISSUES_LIMIT = int(os.getenv("GITHUB_ISSUES_LIMIT", "100"))
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-opus-4-7")
CLAUDE_MAX_TOKENS = int(os.getenv("CLAUDE_MAX_TOKENS", "20000"))