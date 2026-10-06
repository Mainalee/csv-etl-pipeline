import pytest
from src.validators import is_valid_customer_id, parse_age


def test_valid_customer_id():
    assert is_valid_customer_id("CUST_100")


def test_invalid_customer_id():
    assert not is_valid_customer_id("cust100")


def test_parse_age_valid():
    assert parse_age("49") == 49


def test_parse_age_not_a_number():
    with pytest.raises(ValueError):
        parse_age("abc")


def test_parse_age_missing():
    with pytest.raises(ValueError):
        parse_age("")


def test_parse_age_out_of_range():
    with pytest.raises(ValueError):
        parse_age("150")