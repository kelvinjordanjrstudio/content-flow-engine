import typer
from rich import print
from pathlib import Path
from src.parsers.text_parser import TextParser
from src.schema.script import VideoScript, Scene

app = typer.Typer(help="Content Automation & Video Script Engine CLI")

@app.command()
def generate(
    file_path: str = typer.Argument(..., help="Path to the raw text or markdown file to process"),
    platform: str = typer.Option("TikTok", "--platform", "-p", help="Target social media platform")
):
    """Parses raw text and generates a structured video script layout."""
    print(f"[bold cyan]Initializing Content Flow Engine...[/bold cyan]")
    
    try:
        cleaned_text = TextParser.parse_file(file_path)
        print(f"[green]Successfully parsed file:[/green] {file_path}")
        
        # Instantiate a sample structured script demonstrating the schema
        sample_script = VideoScript(
            title=f"Automated Script from {Path(file_path).name}",
            target_platform=platform,
            hook="Stop scrolling and look at this engineering workflow.",
            scenes=[
                Scene(scene_number=1, duration_seconds=4, narration="Here is the core problem we are solving.", visual_description="Close-up terminal view"),
                Scene(scene_number=2, duration_seconds=6, narration=cleaned_text[:100] + "...", visual_description="Highlighted code block")
            ],
            call_to_action="Follow for more backend automation insights."
        )
        
        print("\n[bold yellow]Generated Video Script Schema:[/bold yellow]")
        print(sample_script.model_dump_json(indent=2))
        
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
