from urllib.parse import parse_qs

from api.router import router
from django.conf import settings
from django.test.client import RequestFactory
from django.utils.http import urlencode


def parse_query(raw_query_string, ignore_pagination=True):
    data = {}
    query_string = raw_query_string[:]

    # cut excess
    if 'api/' not in query_string:
        raise AttributeError('Query string has no "api" element.')
    query_string = query_string[query_string.index('api/') + 4 :]

    # get app label
    if '/' not in query_string:
        raise AttributeError('Cant find app label in query string.')
    data['app_label'] = query_string[: query_string.find('/')]
    query_string = query_string[query_string.find('/') + 1 :]

    # get model_plural_name
    if '?' not in query_string:
        raise AttributeError('Cant find model name in query string.')
    data['model_plural_name'] = query_string[: query_string.find('?')]
    query_string = query_string[query_string.find('?') + 1 :]

    # get clean query_params & query_string
    params = parse_qs(query_string, keep_blank_values=True)
    if ignore_pagination:
        params.pop('page', None)
        params.pop('per_page', None)
    data['query_params'] = params
    data['query_string'] = urlencode(params)
    return data


def get_request(request, parsed_data):
    result = RequestFactory().get(
        '/api/{}/{}/'.format(
            parsed_data['app_label'],
            parsed_data['model_plural_name'],
        ),
        parsed_data['query_params'],
    )
    result.user = request.user
    allowed_host = settings.ALLOWED_HOSTS[0]
    if allowed_host != '*':
        result.META['HTTP_X_FORWARDED_HOST'] = allowed_host
        result.META['HTTP_HOST'] = allowed_host
        result.META['SERVER_NAME'] = allowed_host
    return result


def get_view_class(parsed_data):
    for r in router.registry:
        if r[0] == '{}/{}'.format(
            parsed_data['app_label'],
            parsed_data['model_plural_name'],
        ):

            class View(r[1]):
                permission_classes = []

                def dispatch(self, request, *args, **kwargs):
                    result = super().dispatch(request, *args, **kwargs)
                    result.view = self
                    return result

                # def paginate_queryset(self, *args, **kwargs):
                #     return None  noqa E800

            return View
    return None


def get_queryset(view_class, request):
    view_instance = view_class.as_view({'get': 'list'})(request).view
    return view_instance.filter_queryset(view_instance.get_queryset())
