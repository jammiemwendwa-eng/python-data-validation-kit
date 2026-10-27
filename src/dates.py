from datetime import datetime

def validate_iso_date(val: str) -> str:
    try:
        datetime.fromisoformat(val)
        return val
    except ValueError:
        raise ValueError(f"Invalid ISO date: {val}")
