from django.utils.translation import gettext_lazy as _

from common.helpers.fields import create_char_field
from common.helpers.try_get_attr import try_get_attr
from named_views.mixins import NamedViewElementMixin


class NamedFilter(NamedViewElementMixin):
    class Meta:
        verbose_name = _('named filter')
        verbose_name_plural = _('named filters')
        unique_together = (
            'table_type',
            'context',
            'name',
            'user',
        )

    context = create_char_field(
        max_length=250,
        verbose_name=_('context'),
        blank=True,
    )

    def get_existing_entry(self):
        return try_get_attr(
            lambda: self.__class__.objects.get(
                name=self.name, context=self.context, table_type_id=self.table_type_id, user_id=self.user_id
            )
        )
