from .exceptions import ValidationError, MissingFieldError

def validate_schema(data: dict, schema: dict) -> bool:
    for key, validator in schema.items():
        if key not in data:
            raise MissingFieldError(f"Missing: {key}")
        validator(data[key])
    return True
