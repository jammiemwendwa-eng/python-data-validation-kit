import pytest
from src.numbers import validate_positive

def test_validate_positive():
    assert validate_positive(5) == 5
    with pytest.raises(ValueError):
        validate_positive(-1)
