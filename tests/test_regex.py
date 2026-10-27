from src.regex import is_valid_email

def test_is_valid_email():
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("bad-email") is False
