__all__ = (
    'register_model_admins',
    'BaseTableViewAdmin',
    'NamedViewAdmin',
    'NamedFilterAdmin',
    'ContextViewParamsAdmin',
)

from .models import NamedView
from .models.named_view.admin import NamedViewAdmin
from .models import BaseTableView
from .models.base_table_view.admin import BaseTableViewAdmin
from .models import NamedFilter
from .models.named_filter.admin import NamedFilterAdmin
from .models import ContextViewParams
from .models.context_view_params.admin import ContextViewParamsAdmin


def register_model_admins(site):
    site.register(BaseTableView, BaseTableViewAdmin)
    site.register(NamedView, NamedViewAdmin)
    site.register(NamedFilter, NamedFilterAdmin)
    site.register(ContextViewParams, ContextViewParamsAdmin)
