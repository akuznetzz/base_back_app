
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.helpers.AbstractBaseModel import AbstractBaseModel
from common.helpers.fields import create_char_field, create_text_field
from common.helpers.try_get_attr import try_get_attr


class NamedViewElementMixin(AbstractBaseModel):
    class Meta:
        abstract = True

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='+',
    )

    table_type = models.ForeignKey(to=ContentType, verbose_name=_('table_type'), on_delete=models.PROTECT)

    name = create_char_field(
        max_length=50,
        verbose_name=_('view name'),
        blank=True,
    )

    view_text = create_text_field(
        verbose_name=_('view text'),
        help_text=_('View data: JSON object representation for a view data.'),
        blank=True,
    )

    def get_existing_entry(self):
        return try_get_attr(
            lambda: self.__class__.objects.get(name=self.name, table_type_id=self.table_type_id, user_id=self.user_id)
        )

    def save(self, *args, **kwargs):
        if existing_entry := self.get_existing_entry():
            if self.pk is None:
                self.pk = existing_entry.pk
                if 'force_insert' in kwargs:
                    kwargs.pop('force_insert')
                kwargs['force_update'] = True
            elif self.pk != existing_entry.pk:
                raise ValidationError(_('there is already a view with the same name!'))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'id:{self.pk} {self.name}'
