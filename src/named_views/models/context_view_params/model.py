from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.helpers.AbstractBaseModel import AbstractBaseModel
from common.helpers.fields import create_char_field, create_text_field


class ContextViewParams(AbstractBaseModel):
    class Meta:
        verbose_name = _('context view params')
        verbose_name_plural = _('context view params')

    table_type = models.ForeignKey(to=ContentType, verbose_name=_('table_type'), on_delete=models.PROTECT)

    context = create_char_field(verbose_name=_('view context'), max_length=150, blank=True)

    view_params = create_text_field(
        verbose_name=_('view params'),
        help_text=_('View params data: JSON object representation for a view params.'),
        blank=True,
    )
