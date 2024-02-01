from django.db.models import CharField

DEFAULT_PARAMS_CHAR_FIELD = {
    'null': False,
    'default': '',
}


def create_char_field(**kwargs):
    return CharField(**{**DEFAULT_PARAMS_CHAR_FIELD, **kwargs})

def test_func():
    print('Hello world')
