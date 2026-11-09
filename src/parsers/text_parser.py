from pathlib import Path
from typing import Optional

class TextParser:
    @staticmethod
    def parse_file(file_path: str) -> str:
        """Reads a raw text or markdown file and returns cleaned content."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Source file not found: {file_path}")
        
        content = path.read_text(encoding="utf-8")
        return TextParser.clean_text(content)

    @staticmethod
    def clean_text(raw_text: str) -> str:
        """Removes extra whitespace and normalizes line breaks."""
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        return "\n".join(lines)
