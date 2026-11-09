import os
import httpx
import json
from src.schema.script import VideoScriptModel

class LLMClient:
    """Client for generating VideoScriptModel structures via OpenAI REST API."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is not set in environment variables.")
        self.endpoint = "https://api.openai.com/v1/chat/completions"

    def generate_script(self, raw_text: str, platform: str) -> VideoScriptModel:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        schema_structure = {
            "title": "Catchy video title string",
            "platform": platform,
            "hook": {
                "visual_cue": "Description of visual for the hook",
                "spoken_text": "Spoken dialogue/hook text"
            },
            "scenes": [
                {
                    "timestamp": "0:00 - 0:05",
                    "visual": "Visual description",
                    "audio": "Audio or voiceover text",
                    "pacing_notes": "Optional pacing note"
                }
            ],
            "metadata": {
                "estimated_duration_seconds": 30,
                "tags": ["tag1", "tag2"],
                "call_to_action": "CTA text"
            }
        }

        system_prompt = (
            "You are an expert video script architect and content strategist. "
            "Analyze the provided text and convert it into a structured video script JSON object "
            "that strictly adheres to this exact JSON keys and types structure:\n"
            f"{json.dumps(schema_structure, indent=2)}\n"
            "Return ONLY valid JSON matching this schema."
        )

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Platform: {platform}\n\nContent:\n{raw_text}"}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.7
        }

        with httpx.Client(timeout=30.0) as client:
            response = client.post(self.endpoint, headers=headers, json=payload)
            if response.status_code != 200:
                raise RuntimeError(f"OpenAI API Error ({response.status_code}): {response.text}")
            
            data = response.json()
            content_string = data["choices"][0]["message"]["content"]
            
            # Clean up markdown code blocks if model wrapped JSON
            cleaned_content = content_string.strip()
            if cleaned_content.startswith("```json"):
                cleaned_content = cleaned_content[7:]
            if cleaned_content.startswith("```"):
                cleaned_content = cleaned_content[3:]
            if cleaned_content.endswith("```"):
                cleaned_content = cleaned_content[:-3]
            cleaned_content = cleaned_content.strip()

            script_data = json.loads(cleaned_content)
            return VideoScriptModel.model_validate(script_data)