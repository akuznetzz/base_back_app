from django.utils.translation import gettext_lazy as _

from common.helpers.fields import create_char_field
from common.helpers.try_get_attr import try_get_attr
from named_views.mixins import NamedViewElementMixin


class NamedView(NamedViewElementMixin):
    class Meta:
        verbose_name = _('named view')
        verbose_name_plural = _('named views')
        unique_together = (
            'table_type',
            'context',
            'name',
            'user',
        )

    context = create_char_field(verbose_name=_('view context'), max_length=150, blank=True)

    def get_existing_entry(self):
        return try_get_attr(
            lambda: self.__class__.objects.get(
                name=self.name, context=self.context, table_type_id=self.table_type_id, user_id=self.user_id
            )
        )
