class ValidationError(ValueError): pass
class MissingFieldError(ValidationError): pass
class InvalidFormatError(ValidationError): pass
