from pathlib import Path
from src.schema.script import VideoScriptModel

class MarkdownExporter:
    """Renders a validated VideoScriptModel into a production-ready Markdown script file."""
    
    @staticmethod
    def export(script: VideoScriptModel, output_path: Path) -> Path:
        md_lines = [
            f"# {script.title}",
            f"**Platform:** {script.platform}",
            f"**Estimated Duration:** {script.metadata.estimated_duration_seconds} seconds",
            "",
            "## Hook",
            f"- **Visual Cue:** {script.hook.visual_cue}",
            f"- **Spoken Text:** \"{script.hook.spoken_text}\"",
            "",
            "## Scenes",
        ]
        
        for i, scene in enumerate(script.scenes, 1):
            md_lines.extend([
                f"### Scene {i} ({scene.timestamp})",
                f"- **Visual:** {scene.visual}",
                f"- **Audio:** {scene.audio}",
            ])
            if scene.pacing_notes:
                md_lines.append(f"- **Pacing Notes:** {scene.pacing_notes}")
            md_lines.append("")
        
        md_lines.extend([
            "## Metadata & SEO",
            f"- **Tags:** {', '.join(script.metadata.tags)}",
            f"- **Call to Action:** {script.metadata.call_to_action}"
        ])
        
        output_path.write_text("\n".join(md_lines), encoding="utf-8")
        return output_path