"""Core validators using plain Python."""

import re
from dataclasses import dataclass


class ValidationError(ValueError):
    """Raised when a value fails validation."""


@dataclass
class EmailValidator:
    pattern: str = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    def __call__(self, value: str) -> str:
        if not isinstance(value, str):
            raise ValidationError(f"email must be str, got {type(value).__name__}")
        if not re.match(self.pattern, value):
            raise ValidationError(f"invalid email: {value!r}")
        return value.lower()


@dataclass
class PhoneValidator:
    pattern: str = r"^\+?\d{7,15}$"

    def __call__(self, value: str) -> str:
        cleaned = re.sub(r"[\s\-()]", "", value)
        if not re.match(self.pattern, cleaned):
            raise ValidationError(f"invalid phone: {value!r}")
        return cleaned
