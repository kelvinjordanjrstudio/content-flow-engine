from typing import Dict, Any

class PromptBuilder:
    """Constructs system and user prompts for generating structured short-form video scripts."""
    
    @staticmethod
    def build_system_prompt() -> str:
        return (
            "You are an expert short-form content creator and script architect. "
            "Your task is to transform unstructured text into a high-converting, highly structured "
            "video script breakdown optimized for audience retention, clear pacing, and strict metadata rules."
        )

    @staticmethod
    def build_user_prompt(parsed_text: str, platform: str) -> str:
        return (
            f"Target Platform: {platform}\n\n"
            f"Source Text / Content:\n{parsed_text}\n\n"
            "Analyze this text and output a JSON object matching the required schema containing:\n"
            "1. Title and target platform.\n"
            "2. An attention-grabbing hook (with visual cue and spoken text).\n"
            "3. A breakdown of sequential scenes (each with timestamp, visual instruction, audio script, and pacing notes).\n"
            "4. Content metadata including estimated duration, target tags, and a call to action."
        )