from pathlib import Path
from src.schema.script import VideoScriptModel

class JsonExporter:
    """Exports a validated VideoScriptModel to a formatted JSON file."""
    
    @staticmethod
    def export(script: VideoScriptModel, output_path: Path) -> Path:
        output_path.write_text(script.model_dump_json(indent=2), encoding="utf-8")
        return output_path