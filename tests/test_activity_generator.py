import pytest

from activity_generator import validate_date


def test_valid_date():
    assert validate_date("2026-08-25") == "2026-08-25"


def test_invalid_calendar_date():
    with pytest.raises(Exception):
        validate_date("2026-02-30")


def test_invalid_date_format():
    with pytest.raises(Exception):
        validate_date("25-08-2026")
