from typing import Dict

class TextParser:
    """Parses raw input text into distinct structural components."""

    @staticmethod
    def parse(raw_text: str) -> Dict[str, str]:
        """Splits raw text into sections based on headers or simple paragraph blocks."""
        sections = {}
        current_section = "general"
        current_lines = []

        for line in raw_text.splitlines():
            stripped = line.strip()
            # Detect header patterns like [TITLE], TITLE:, or # TITLE
            if stripped.startswith("[") and stripped.endswith("]"):
                if current_lines:
                    sections[current_section] = "\n".join(current_lines).strip()
                    current_lines = []
                current_section = stripped[1:-1].lower()
            elif stripped.endswith(":") and len(stripped) < 30:
                if current_lines:
                    sections[current_section] = "\n".join(current_lines).strip()
                    current_lines = []
                current_section = stripped[:-1].lower()
            else:
                current_lines.append(line)

        if current_lines:
            sections[current_section] = "\n".join(current_lines).strip()

        # Fallback if no specific headers were found
        if not sections or (len(sections) == 1 and "general" in sections):
            sections = {
                "raw_content": raw_text.strip(),
                "summary": raw_text[:200] + "..." if len(raw_text) > 200 else raw_text
            }

        return sections