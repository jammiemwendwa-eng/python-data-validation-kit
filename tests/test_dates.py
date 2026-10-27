import pytest
from src.dates import validate_iso_date

def test_validate_iso_date():
    assert validate_iso_date("2026-10-27") == "2026-10-27"
    with pytest.raises(ValueError):
        validate_iso_date("not-a-date")
