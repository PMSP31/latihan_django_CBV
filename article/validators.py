from django.core.exceptions import ValidationError

def validate_title(value) :
    if value == "abc":
        raise ValidationError("Title Article Can't Empty")
    else :
        return value