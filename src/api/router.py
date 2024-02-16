from dynamic_rest import routers

from app.viewsets import PersonViewSet
from common.helpers.get_model_meta import get_model_meta
from named_views.models.base_table_view.viewset import BaseTableViewViewSet
from named_views.models.context_view_params.viewset import ContextViewParamsViewSet
from named_views.models.named_filter.viewset import NamedFilterViewSet
from named_views.models.named_view.viewset import NamedViewViewSet


router = routers.DynamicRouter()


def register(*views):
    for view in views:

        class View(
            view,
        ):
            pass

        router.register(
            f'{get_model_meta(view).app_label.replace("_", "")}/{view.serializer_class.get_plural_name()}', View
        )


register(

    PersonViewSet,

    # named_views
    BaseTableViewViewSet,
    NamedViewViewSet,
    NamedFilterViewSet,
    ContextViewParamsViewSet,

)
