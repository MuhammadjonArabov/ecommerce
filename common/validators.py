from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


def phone_number_validator():
    validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Phone number must be entered in the format: '+998xx xxx xx xx. Up to 15 digits allowed.")
    )
    return validator
