import os
from exceptions import ClaudeClientError, ClaudeConnectionError
from anthropic import Anthropic, APIError, APIConnectionError
from typing import Dict, Any
from dotenv import load_dotenv

def send_claude_request(
    prompt: str,
    system_prompt: str = None,
    model: str = "claude-opus-4-7",
    max_tokens: int = 50000
) -> str:
    
    load_dotenv()
    api_key = os.getenv("CLAUDE_API")

    if not api_key:
        raise ClaudeClientError("missing CLAUDE_API in environment variables.")

    try:
        client = Anthropic(api_key=api_key)
        
        kwargs: Dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        if system_prompt:
            kwargs["system"] = system_prompt
            
        message = client.messages.create(**kwargs)
        
        if message.content:
            return message.content[0].text
            
        return ""

    except APIConnectionError as e:
         raise ClaudeConnectionError("connection to claude API failed") from e
    except APIError as e:
         raise ClaudeClientError(f"claude API error: {e.message}") from e
    except Exception as e:
         raise ClaudeClientError(f"unexpected error: {str(e)}") from e