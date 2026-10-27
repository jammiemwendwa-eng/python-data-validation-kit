from src.engine import validate_schema
from src.numbers import validate_positive

def test_validate_schema():
    assert validate_schema({"age": 5}, {"age": validate_positive})
