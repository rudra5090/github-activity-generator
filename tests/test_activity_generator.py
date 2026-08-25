from datetime import datetime


def parse_commit_date(value):
    return datetime.strptime(value, "%Y-%m-%d").strftime("%Y-%m-%dT12:00:00")


def test_valid_date():
    assert parse_commit_date("2026-08-25") == "2026-08-25T12:00:00"


def test_invalid_calendar_date():
    try:
        parse_commit_date("2026-02-30")
        assert False
    except ValueError:
        assert True


def test_invalid_date_format():
    try:
        parse_commit_date("25-08-2026")
        assert False
    except ValueError:
        assert True
