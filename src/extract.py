import csv

def extract(path):
    """Read a CSV file and return a list of row dictionaries."""
    try:
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        raise SystemExit(f"Input file not found: {path}")