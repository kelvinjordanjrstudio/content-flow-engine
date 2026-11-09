import pytest
from unittest.mock import patch, MagicMock
from src.generators.prompt_builder import PromptBuilder
from src.generators.llm_client import LLMClient
from src.schema.script import VideoScriptModel

def test_prompt_builder():
    """Verify system and user prompts format correctly."""
    sys_prompt = PromptBuilder.build_system_prompt()
    user_prompt = PromptBuilder.build_user_prompt("Test input content", "TikTok")
    
    assert "expert short-form content creator" in sys_prompt
    assert "Target Platform: TikTok" in user_prompt
    assert "Test input content" in user_prompt

@patch("src.generators.llm_client.httpx.Client")
def test_llm_client_generation(mock_httpx_client):
    """Verify LLMClient correctly sends payloads and parses responses into VideoScriptModel."""
    
    # Mock the JSON response structure matching our Pydantic schema
    mock_response_data = {
        "choices": [
            {
                "message": {
                    "content": """{
                        "title": "Test Script",
                        "platform": "TikTok",
                        "hook": {
                            "visual_cue": "Close up on screen",
                            "spoken_text": "Stop scrolling right now."
                        },
                        "scenes": [
                            {
                                "timestamp": "0:00 - 0:03",
                                "visual": "Show code editor",
                                "audio": "Look at how fast this builds.",
                                "pacing_notes": "Fast cuts"
                            }
                        ],
                        "metadata": {
                            "estimated_duration_seconds": 15,
                            "tags": ["coding", "python"],
                            "call_to_action": "Follow for more."
                        }
                    }"""
                }
            }
        ]
    }

    # Setup mock behavior
    mock_instance = mock_httpx_client.return_value.__enter__.return_value
    mock_post_res = MagicMock()
    mock_post_res.status_code = 200
    mock_post_res.json.return_value = mock_response_data
    mock_post_res.raise_for_status.return_value = None
    mock_instance.post.return_value = mock_post_res

    # Initialize client with a dummy key
    client = LLMClient(api_key="fake-test-key")
    result = client.generate_script("Some raw text content", "TikTok")

    # Assertions to ensure it maps properly to the Pydantic schema
    assert isinstance(result, VideoScriptModel)
    assert result.title == "Test Script"
    assert result.platform == "TikTok"
    assert result.hook.spoken_text == "Stop scrolling right now."
    assert len(result.scenes) == 1
    assert result.metadata.estimated_duration_seconds == 15