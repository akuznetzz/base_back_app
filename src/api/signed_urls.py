import functools

from django.core.signing import dumps, loads
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import User

SALT = 'ipM84wKQTnJhJPLDLYHwpzqwURkPa9iQ'  # salt for cryptographic
MAX_KEY_AGE = 30  # lifetime of the access key in seconds

CONTENTS_USER_ID = 'user_id'
CONTENTS_URL = 'url'
REQ_PARAM_PROTECTED_KEY = 'key'


class SignedUrlsView(APIView):
    """ Endpoint for request the access key """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return Response(
            dumps(
                {
                    CONTENTS_USER_ID: request.user.id,
                    CONTENTS_URL: request.data[CONTENTS_URL]
                },
                salt=SALT,
                compress=True
            ),
            status=status.HTTP_200_OK
        )


class KeyProtected(BasePermission):
    """ Permission class for API Views. Must be specified before IsAuthenticated """

    def has_permission(self, request, view):
        assign_user_from_key(request, request.query_params)
        return True


def assign_user_from_key(request, params):
    key_data: str = params.get(REQ_PARAM_PROTECTED_KEY)
    if key_data:
        try:
            content = loads(key_data, salt=SALT, max_age=30)
            if content[CONTENTS_URL] in request.path:
                user = User.objects.get(pk=content[CONTENTS_USER_ID])
                if user.is_active:
                    request.user = user
        except Exception:  # Yes, yes, we suppress any exception in our small authentication
            pass


def key_protected(func):
    """ Decorator function for django views. Must be specified before login_required decorator """

    @functools.wraps(func)
    def decorated(request, *args, **kwargs):
        assign_user_from_key(request, request.GET)
        return func(request, *args, **kwargs)

    return decorated
