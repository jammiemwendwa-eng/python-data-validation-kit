def validate_positive(val: float) -> float:
    if val <= 0: raise ValueError("Must be positive")
    return val
