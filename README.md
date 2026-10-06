# CSV Data Cleaning, Validation & ETL Pipeline

A command-line ETL (Extract-Transform-Load) pipeline in Python that reads a messy customer CSV file, cleans and validates each record, and writes a clean dataset plus an audit log of every rejected row.

## Key Features
- Reads raw CSV data with the built-in `csv` module
- Trims whitespace and standardizes IDs
- Validates customer ID format, segment, region, and age
- Detects duplicate customer IDs
- Logs every rejected row with its line number and reason
- Writes a production-ready clean CSV

## Concepts Used
File I/O, string handling, regular expressions, exception handling, modular code design (separate extract, transform, and load modules).

## Project Structure
```text
csv-etl-pipeline/
├── src/
│   ├── main.py         # Entry point
│   ├── extract.py      # Reads the raw CSV
│   ├── validators.py   # Small validation functions
│   ├── transform.py    # Cleaning and filtering logic
│   └── load.py         # Writes the clean CSV and error log
├── data/
│   └── raw_customers.csv
├── .gitignore
└── README.md
```

## How to Run
1. Make sure Python 3 is installed.
2. Clone the repository and open a terminal in the project folder.
3. Run:
```bash
   python -m src.main
```
The program uses only the Python standard library, so there is nothing to install.

## Sample Output
```text
Read:     9 rows
Cleaned:  7 rows -> data/clean_customers.csv
Rejected: 2 rows -> data/errors.log
```

Example `errors.log`:
```text
Run at 2026-10-06 14:32:10
Line 6: missing customer_segment
Line 10: missing customer_segment
```
   ## Run the Tests
```bash
   pip install pytest
   python -m pytest
```