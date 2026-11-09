import typer
from rich import print
from pathlib import Path
from src.parsers.text_parser import TextParser
from src.generators.llm_client import LLMClient
from src.exporters.json_exporter import JsonExporter
from src.exporters.markdown_exporter import MarkdownExporter

app = typer.Typer(
    help="Content Flow Engine CLI - Parse, generate, and export video script architectures.",
    no_args_is_help=True
)

@app.callback()
def main():
    """Content Flow Engine CLI"""
    pass

@app.command(name="parse")
def parse_file(
    file_path: Path = typer.Argument(..., help="Path to the raw input text file.")
):
    """Parse an unstructured text file into structural blocks."""
    if not file_path.exists():
        print(f"[bold red]Error:[/bold red] File '{file_path}' not found.")
        raise typer.Exit(code=1)

    print(f"[bold cyan]Reading content from:[/bold cyan] {file_path}")
    raw_text = file_path.read_text(encoding="utf-8")
    
    parsed_sections = TextParser.parse(raw_text)
    
    print("[bold green]Successfully parsed text structure:[/bold green]")
    for section, content in parsed_sections.items():
        print(f"\n[bold yellow]{section.upper()}:[/bold yellow]\n{content}")

@app.command(name="generate")
def generate_script(
    file_path: Path = typer.Argument(..., help="Path to the raw input text file."),
    platform: str = typer.Option("TikTok", "--platform", "-p", help="Target social platform (e.g. TikTok, Reels, Shorts)."),
    format: str = typer.Option("markdown", "--format", "-f", help="Export format: 'markdown' or 'json'."),
    output: Path = typer.Option(Path("output.md"), "--output", "-o", help="Path for the output file.")
):
    """Generate a structured video script using the LLM pipeline and export it."""
    if not file_path.exists():
        print(f"[bold red]Error:[/bold red] File '{file_path}' not found.")
        raise typer.Exit(code=1)

    print(f"[bold cyan]Reading source content from:[/bold cyan] {file_path}")
    raw_text = file_path.read_text(encoding="utf-8")
    
    # Step 1: Parse
    parsed_sections = TextParser.parse(raw_text)
    combined_content = "\n".join(parsed_sections.values())

    print(f"[bold cyan]Generating script via LLM client for platform:[/bold cyan] {platform}")
    try:
        client = LLMClient()
        script_model = client.generate_script(combined_content, platform)
    except Exception as e:
        print(f"[bold red]Generation Error:[/bold red] {e}")
        raise typer.Exit(code=1)

    # Step 2: Export
    if format.lower() == "json":
        saved_path = JsonExporter.export(script_model, output)
    elif format.lower() in ["markdown", "md"]:
        saved_path = MarkdownExporter.export(script_model, output)
    else:
        print(f"[bold red]Error:[/bold red] Unsupported format '{format}'. Use 'markdown' or 'json'.")
        raise typer.Exit(code=1)

    print(f"[bold green]Successfully exported validated script to:[/bold green] {saved_path}")

if __name__ == "__main__":
    app()