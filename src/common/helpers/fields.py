from decimal import Decimal

from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import TextField

DEFAULT_PARAMS_DECIMAL_FIELD = {
    'max_digits': 12,
    'decimal_places': 2,
}
DEFAULT_PARAMS_CHAR_FIELD = {
    'null': False,
    'default': '',
}
DEFAULT_PARAMS_TEXT_FIELD = {
    **DEFAULT_PARAMS_CHAR_FIELD,
}


def create_money_field(zero_as_default=True, **kwargs):
    """Factory function for money field"""

    default = Decimal('0') if zero_as_default else None
    return DecimalField(**{**{**DEFAULT_PARAMS_DECIMAL_FIELD, **{'default': default}}, **kwargs})


def create_char_field(**kwargs):
    return CharField(**{**DEFAULT_PARAMS_CHAR_FIELD, **kwargs})


def create_text_field(**kwargs):
    return TextField(**{**DEFAULT_PARAMS_TEXT_FIELD, **kwargs})
