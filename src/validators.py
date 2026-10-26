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
from datetime import date, datetime


@dataclass
class DateValidator:
    min_date: date | None = None
    max_date: date | None = None

    def __call__(self, value: str) -> date:
        try:
            d = datetime.fromisoformat(value).date()
        except ValueError as e:
            raise ValidationError(f"invalid ISO date: {value!r}") from e
        if self.min_date and d < self.min_date:
            raise ValidationError(f"date {d} before min {self.min_date}")
        if self.max_date and d > self.max_date:
            raise ValidationError(f"date {d} after max {self.max_date}")
        return d


def validate_all(value: dict, rules: dict) -> dict:
    """Apply each validator in rules to matching keys in value."""
    errors: dict[str, str] = {}
    cleaned: dict = {}
    for key, validator in rules.items():
        if key not in value:
            errors[key] = "missing"
            continue
        try:
            cleaned[key] = validator(value[key])
        except ValidationError as e:
            errors[key] = str(e)
    if errors:
        raise ValidationError(f"validation failed: {errors}")
    return cleaned
