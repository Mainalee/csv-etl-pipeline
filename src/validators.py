import re

ID_PATTERN = re.compile(r"^CUST_\d+$")
VALID_SEGMENTS = {"Consumer", "SMB", "Enterprise"}
VALID_REGIONS = {"APAC", "EMEA", "LATAM", "North America"}


def is_valid_customer_id(value):
    """True if the id looks like CUST_ followed by digits."""
    return bool(ID_PATTERN.match(value))


def parse_age(value):
    """Turn age text into a number, or raise ValueError with a reason."""
    if not value:
        raise ValueError("missing age")
    try:
        age = int(value)
    except ValueError:
        raise ValueError(f"age is not a number: '{value}'")
    if not 0 < age < 120:
        raise ValueError(f"age out of range: {age}")
    return age