from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.models.person import Person
from app.models.user.UserManager import UserManager
from utils.mixins.TimestampMixin import TimestampMixin


class User(AbstractUser, TimestampMixin):
    class Meta(AbstractUser.Meta):
        default_related_name = 'users'

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    first_name = None
    last_name = None

    objects = UserManager()

    person = models.ForeignKey(
        verbose_name=_('person'),
        to=Person,
        related_name='users',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )