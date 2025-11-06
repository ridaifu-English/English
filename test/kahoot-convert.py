#!/usr/bin/env python3
"""
Convert Kahoot CSV quiz file to Excel format (.xlsx)
Usage: python kahoot-convert.py <input_csv_path> <output_xlsx_path>
"""

import sys
import pandas as pd
from pathlib import Path


def convert_csv_to_excel(csv_path: str, xlsx_path: str) -> None:
    """
    Convert a CSV file to Excel format.
    
    Args:
        csv_path: Path to input CSV file
        xlsx_path: Path to output Excel file
    """
    # Read CSV file
    df = pd.read_csv(csv_path, header=None)
    
    # Write to Excel
    df.to_excel(xlsx_path, index=False, header=False, engine='openpyxl')
    
    print(f"✓ Successfully converted '{csv_path}' to '{xlsx_path}'")


def main():
    if len(sys.argv) != 3:
        print("Usage: python kahoot-convert.py <input_csv_path> <output_xlsx_path>")
        print("\nExample:")
        print("  python kahoot-convert.py vocabulary-kahoot-quiz.csv vocabulary-kahoot-quiz.xlsx")
        sys.exit(1)
    
    csv_path = sys.argv[1]
    xlsx_path = sys.argv[2]
    
    # Check if input file exists
    if not Path(csv_path).exists():
        print(f"Error: Input file '{csv_path}' not found")
        sys.exit(1)
    
    # Ensure output has .xlsx extension
    if not xlsx_path.endswith('.xlsx'):
        xlsx_path += '.xlsx'
    
    try:
        convert_csv_to_excel(csv_path, xlsx_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

