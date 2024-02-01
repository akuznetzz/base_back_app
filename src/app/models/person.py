from django.db import models

from django.utils.translation import gettext_lazy as _

from common.helpers.AbstractBaseModel import AbstractBaseModel
from common.helpers.create_char_field import create_char_field


class Person(AbstractBaseModel):
    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    last_name = models.CharField(max_length=255, verbose_name=_('last name'))
    first_name = create_char_field(max_length=255, verbose_name=_('first name'), blank=True)
    middle_name = create_char_field(max_length=255, verbose_name=_('patronymic'), blank=True)
    birth_date = models.DateField(verbose_name=_('birth date'), null=True, blank=True)
    birth_place = create_char_field(max_length=255, verbose_name=_('birth place'), blank=True)

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.middle_name}'
