import csv
from datetime import datetime


def write_clean_csv(rows, path):
    """Save cleaned rows to a CSV file."""
    fields = ["customer_id", "customer_segment", "region", "age"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_error_log(errors, path):
    """Save rejected rows and the reason for each to a log file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Run at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
        for line_no, reason in errors:
            f.write(f"Line {line_no}: {reason}\n")