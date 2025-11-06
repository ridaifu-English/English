# Kahoot CSV to Excel Converter

Simple script to convert Kahoot quiz CSV files to Excel (.xlsx) format for uploading to Kahoot.

## Setup with uv

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
```

No additional setup needed! `uv run` will automatically install dependencies.

## Usage

```bash
# Navigate to the test directory
cd test

# Run with uv (automatically installs dependencies)
uv run --with pandas --with openpyxl python kahoot-convert.py <input.csv> <output.xlsx>
```

## Example

Convert the vocabulary quiz:
```bash
cd test
uv run --with pandas --with openpyxl python kahoot-convert.py ../GS/midterm-20251016/vocabulary-kahoot-quiz.csv ../GS/midterm-20251016/vocabulary-kahoot-quiz.xlsx
```

Or from any directory:
```bash
cd /Users/akitamasaki/Documents/ridaifu/English/test
uv run --with pandas --with openpyxl python kahoot-convert.py ../GS/midterm-20251016/vocabulary-kahoot-quiz.csv ../GS/midterm-20251016/vocabulary-kahoot-quiz.xlsx
```

The output file can then be uploaded directly to Kahoot.

