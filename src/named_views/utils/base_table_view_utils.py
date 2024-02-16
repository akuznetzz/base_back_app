import json
from datetime import datetime

from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from app.models import User
from common.helpers.try_get_attr import try_get_attr
from named_views.models import BaseTableView
from named_views.models import ContextViewParams
from named_views.models import NamedView
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST

TABLE_ID_KEY = 'table_id'
CONTEXT_KEY = 'context'
UPDATE_DTIME_KEY = 'update_dtime'
RESPONSE_VIEW_TEXT_KEY = 'view_text'
RESPONSE_VIEW_PARAMS_KEY = 'view_params'
EMPTY_VIEW_TEXT = '{"available_fields":[{"field":"id"}]}'

MSG_REQUEST_PARAMETERS_NOT_DEFINED = _('Request parameters not defined.')


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_fresh_base_table_view_data(request):
    params = json.loads(request.body)
    if TABLE_ID_KEY not in params:
        return HttpResponse(content=str(MSG_REQUEST_PARAMETERS_NOT_DEFINED), status=HTTP_400_BAD_REQUEST)
    table_id = params[TABLE_ID_KEY]
    base_table_views = BaseTableView.objects.filter(table_type=table_id)
    user_context = try_get_attr(lambda: User.objects.get(id=request.user.id).user_right_context, '')
    if user_context is None:
        view_text = EMPTY_VIEW_TEXT
    else:
        base_table_views = base_table_views.filter(context=user_context)
        if params.get(UPDATE_DTIME_KEY):
            update_dtime = datetime.strptime(params[UPDATE_DTIME_KEY], '%d.%m.%Y %H:%M:%S')
            base_table_views = base_table_views.filter(updated__gt=update_dtime)
        view_text = (
            base_table_views.first().view_text
            if base_table_views.exists()
            else None
            if not user_context
            else EMPTY_VIEW_TEXT
        )

    return HttpResponse(
        content=json.dumps(
            {
                RESPONSE_VIEW_TEXT_KEY: view_text,
            },
            ensure_ascii=False,
        ),
        status=HTTP_200_OK,
    )


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_fresh_context_view_params_data(request):
    params = json.loads(request.body)
    if TABLE_ID_KEY not in params:
        return HttpResponse(content=str(MSG_REQUEST_PARAMETERS_NOT_DEFINED), status=HTTP_400_BAD_REQUEST)
    table_id = params[TABLE_ID_KEY]
    context = params.get(CONTEXT_KEY, '')
    context_view_params = ContextViewParams.objects.filter(table_type=table_id, context=context)
    if params.get(UPDATE_DTIME_KEY):
        update_dtime = datetime.strptime(params[UPDATE_DTIME_KEY], '%d.%m.%Y %H:%M:%S')
        context_view_params = context_view_params.filter(updated__gt=update_dtime)
    view_params = context_view_params.first().view_params if context_view_params.exists() else None

    return HttpResponse(
        content=json.dumps(
            {
                RESPONSE_VIEW_PARAMS_KEY: view_params,
            },
            ensure_ascii=False,
        ),
        status=HTTP_200_OK,
    )


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_fresh_default_table_view_descr(request):
    params = json.loads(request.body)
    if TABLE_ID_KEY not in params:
        return HttpResponse(content=str(MSG_REQUEST_PARAMETERS_NOT_DEFINED), status=HTTP_400_BAD_REQUEST)
    table_id = params[TABLE_ID_KEY]
    user_context = try_get_attr(lambda: User.objects.get(id=request.user.id).user_right_context, '')
    default_table_views = NamedView.objects.filter(table_type=table_id, user__isnull=True, name='', context=user_context)
    if params.get(UPDATE_DTIME_KEY):
        update_dtime = datetime.strptime(params[UPDATE_DTIME_KEY], '%d.%m.%Y %H:%M:%S')
        default_table_views = default_table_views.filter(updated__gt=update_dtime)
    view_text = default_table_views.first().view_text if default_table_views.exists() else None

    return HttpResponse(
        content=json.dumps(
            {
                RESPONSE_VIEW_TEXT_KEY: view_text,
            },
            ensure_ascii=False,
        ),
        status=HTTP_200_OK,
    )
