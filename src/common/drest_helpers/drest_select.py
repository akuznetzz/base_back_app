import json
from decimal import Decimal

from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST

from common.drest_helpers.drest_parser import parse_query, get_view_class, get_request

QUERY_PARAM = 'query'


class SelectExportEncoder(json.JSONEncoder):
    def default(self, encod_val):
        if isinstance(encod_val, Decimal):
            return str(encod_val)
        if isinstance(encod_val, set):
            return list(encod_val)
        return super().default(encod_val)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def drest_select_enpoint(request):
    # parse body
    json_data = json.loads(request.body)
    if QUERY_PARAM not in json_data or not json_data[QUERY_PARAM]:
        return HttpResponse(content=str(_('Invalid QUERY_PARAM data.')), status=HTTP_400_BAD_REQUEST)
    raw_query = json_data[QUERY_PARAM]

    try:
        parsed_data = parse_query(raw_query, False)
    except AttributeError as e:
        return HttpResponse(content=str(e), status=HTTP_400_BAD_REQUEST)

    view_class = get_view_class(parsed_data)
    prepared_request = get_request(request, parsed_data)
    view_instance = view_class.as_view({'get': 'list'})(prepared_request)

    return HttpResponse(
        content=json.dumps(view_instance.data, cls=SelectExportEncoder, ensure_ascii=False),
        status=HTTP_200_OK,
    )
