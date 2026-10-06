from src.validators import (
    is_valid_customer_id,
    parse_age,
    VALID_SEGMENTS,
    VALID_REGIONS,
)

def clean_row(row):
    """Clean one row. Raise ValueError (with a reason) if it can't be fixed."""
    customer_id = row["customer_id"].strip().upper()
    if not is_valid_customer_id(customer_id):
        raise ValueError(f"invalid customer_id: '{customer_id}'")

    segment = row["customer_segment"].strip()
    if not segment:
        raise ValueError("missing customer_segment")
    if segment not in VALID_SEGMENTS:
        raise ValueError(f"unknown customer_segment: '{segment}'")

    region = row["region"].strip()
    if not region:
        raise ValueError("missing region")
    if region not in VALID_REGIONS:
        raise ValueError(f"unknown region: '{region}'")

    return {
        "customer_id": customer_id,
        "customer_segment": segment,
        "region": region,
        "age": parse_age(row["age"].strip()),
    }


def transform(rows):
    """Return (clean_rows, errors). Errors are (line_number, reason) pairs."""
    clean, errors = [], []
    seen_ids = set()

    for line_no, row in enumerate(rows, start=2):  # line 1 is the header
        try:
            cleaned = clean_row(row)
        except ValueError as e:
            errors.append((line_no, str(e)))
            continue

        if cleaned["customer_id"] in seen_ids:
            errors.append((line_no, f"duplicate customer_id: {cleaned['customer_id']}"))
            continue

        seen_ids.add(cleaned["customer_id"])
        clean.append(cleaned)

    return clean, errors