from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.helpers.AbstractBaseModel import AbstractBaseModel
from common.helpers.fields import create_text_field, create_char_field


class BaseTableView(AbstractBaseModel):
    class Meta:
        verbose_name = _('base table view')
        verbose_name_plural = _('base table views')

    table_type = models.ForeignKey(to=ContentType, verbose_name=_('table_type'), on_delete=models.PROTECT)

    view_text = create_text_field(
        verbose_name=_('view text'),
        help_text=_('View data: JSON object representation for a view data.'),
        blank=True,
    )

    context = create_char_field(verbose_name=_('view context'), max_length=150, blank=True)
