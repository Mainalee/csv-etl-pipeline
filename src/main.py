from src.extract import extract
from src.transform import transform
from src.load import write_clean_csv, write_error_log

RAW_PATH = "data/raw_customers.csv"
CLEAN_PATH = "data/clean_customers.csv"
ERROR_PATH = "data/errors.log"


def main():
    rows = extract(RAW_PATH)
    clean, errors = transform(rows)
    write_clean_csv(clean, CLEAN_PATH)
    write_error_log(errors, ERROR_PATH)

    print(f"Read:     {len(rows)} rows")
    print(f"Cleaned:  {len(clean)} rows -> {CLEAN_PATH}")
    print(f"Rejected: {len(errors)} rows -> {ERROR_PATH}")


if __name__ == "__main__":
    main()