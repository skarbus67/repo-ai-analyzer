from exceptions import ClaudeClientError, ClaudeConnectionError
from anthropic import Anthropic, APIError, APIConnectionError
from typing import Dict, Any
from config import CLAUDE_MODEL, CLAUDE_MAX_TOKENS, ANTHROPIC_API_KEY

def send_claude_request(
    prompt: str,
    system_prompt: str = None,
) -> str:
    
    try:
        client = Anthropic(api_key=ANTHROPIC_API_KEY)
        
        kwargs: Dict[str, Any] = {
            "model": CLAUDE_MODEL,
            "max_tokens": CLAUDE_MAX_TOKENS,
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