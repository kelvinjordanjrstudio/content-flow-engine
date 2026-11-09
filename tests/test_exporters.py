import pytest
from pathlib import Path
from src.schema.script import VideoScriptModel, HookModel, SceneModel, MetadataModel
from src.exporters.json_exporter import JsonExporter
from src.exporters.markdown_exporter import MarkdownExporter

@pytest.fixture
def sample_script():
    return VideoScriptModel(
        title="Test Video Script",
        platform="TikTok",
        hook=HookModel(visual_cue="Close up on camera", spoken_text="Stop scrolling right now."),
        scenes=[
            SceneModel(timestamp="0:00 - 0:05", visual="Show code editor", audio="Look at how fast this builds.", pacing_notes="Fast cuts")
        ],
        metadata=MetadataModel(estimated_duration_seconds=15, tags=["python", "coding"], call_to_action="Follow for more.")
    )

def test_json_exporter(sample_script, tmp_path):
    """Verify script exports to valid JSON and validates back correctly."""
    out_file = tmp_path / "script.json"
    JsonExporter.export(sample_script, out_file)
    assert out_file.exists()
    
    loaded = VideoScriptModel.model_validate_json(out_file.read_text(encoding="utf-8"))
    assert loaded.title == "Test Video Script"
    assert loaded.platform == "TikTok"

def test_markdown_exporter(sample_script, tmp_path):
    """Verify script exports to correctly formatted Markdown."""
    out_file = tmp_path / "script.md"
    MarkdownExporter.export(sample_script, out_file)
    assert out_file.exists()
    
    content = out_file.read_text(encoding="utf-8")
    assert "# Test Video Script" in content
    assert "**Platform:** TikTok" in content
    assert "Close up on camera" in content
    assert "Show code editor" in content