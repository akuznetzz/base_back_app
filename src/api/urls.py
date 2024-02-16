from django.urls import include
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from api.me import MeView
from api.router import router
from api.signed_urls import SignedUrlsView
from auth.views import TokenObtainPairView
from common.drest_helpers.drest_select import drest_select_enpoint
from named_views.utils import get_fresh_base_table_view_data
from named_views.utils.base_table_view_utils import get_fresh_context_view_params_data
from named_views.utils.base_table_view_utils import get_fresh_default_table_view_descr

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/me/', MeView.as_view()),
    path('auth/sign_url/', SignedUrlsView.as_view()),
    path('get-fresh-base-table-view-data/', get_fresh_base_table_view_data, name='get_fresh_base_table_view_data'),
    path(
        'get-fresh-context-view-params-data/',
        get_fresh_context_view_params_data,
        name='get_fresh_context_view_params_data',
    ),
    path(
        'get_fresh_default_table_view_descr/',
        get_fresh_default_table_view_descr,
        name='get_fresh_default_table_view_descr',
    ),
    path('drest-select/', drest_select_enpoint, name='drest_select'),

]
