# Content Flow Engine CLI

A production-grade command-line interface (CLI) for parsing unstructured text and generating structured, platform-optimized video scripts using OpenAI's `gpt-4o-mini` with strict Pydantic schema validation.

## Features

- **Structural Text Parsing**: Converts raw input files into structured textual blocks.
- **Strict Data Contracts**: Uses Pydantic models (`VideoScriptModel`) to guarantee strict output schemas across scenes, visual cues, audio, and metadata.
- **REST-Native LLM Client**: Built with `httpx` to interface directly with OpenAI APIs without heavy SDK overhead.
- **Multi-Format Exporting**: Supports output generation in both Markdown and JSON formats.
- **Robust CLI Architecture**: Built using `Typer` and `Rich` for clear terminal UX and error handling.

## Project Structure

```text
content-flow-engine/
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── schema/
│   │   ├── __init__.py
│   │   └── script.py
│   ├── parsers/
│   │   ├── __init__.py
│   │   └── text_parser.py
│   ├── generators/
│   │   ├── __init__.py
│   │   └── llm_client.py
│   └── exporters/
│       ├── __init__.py
│       ├── json_exporter.py
│       └── markdown_exporter.py
├── tests/
│   ├── test_exporters.py
│   └── test_generator.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository and navigate to the project root:
```bash
git clone <repository-url>
cd content-flow-engine
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your OpenAI API key:
```bash
# Windows PowerShell
$env:OPENAI_API_KEY="your-api-key-here"

# macOS/Linux
export OPENAI_API_KEY="your-api-key-here"
```

## Usage Run Script Generation
Generate a video script from a source text file:
```bash
python -m src.cli generate sample.txt --platform TikTok --format markdown --output script_output.md
```
Options:

- --platform: Target platform (e.g., TikTok, YouTube Shorts, Instagram Reels).

- --format: Output format (markdown or json). Default is markdown.

- --output: File path to write the formatted script output.

Run Testing Suite
Execute unit tests with pytest:
```bash
python -m pytest -v
```

## Architecture & Data Schema
The generation flow enforces strict type safety end-to-end:

1. `TextParser` extracts and cleans raw source text.

2. `LLMClient` sends structured system instructions to OpenAI via direct `httpx` POST calls with `response_format={"type": "json_object"}`.

3. Raw API output is parsed directly into `VideoScriptModel` Pydantic models.

4. Exporters convert validated models into desired target output formats.