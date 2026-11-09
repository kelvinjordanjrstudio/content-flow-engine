# Content Flow Engine (content-flow-engine)

A modular Python command-line engine designed to parse unstructured text and generate structured video script architectures, hooks, and scene breakdowns for automated content pipelines.

## Features
* **Modular Architecture:** Clean separation of concerns across text parsing, validation schemas, and CLI commands.
* **Strict Data Schemas:** Built with Pydantic to enforce precise formatting for short-form video hooks, pacing, and metadata.
* **CLI Interface:** Built with Typer and Rich for seamless terminal execution and formatted output.

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/content-flow-engine.git
   cd content-flow-engine
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows (PowerShell):
   .\venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script generator CLI:
```bash
python -m src.cli sample.txt --platform TikTok
```

## License
MIT
