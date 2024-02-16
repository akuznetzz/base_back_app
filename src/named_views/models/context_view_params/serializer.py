from django.utils.translation import gettext_lazy as _
from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField

from .model import ContextViewParams
from ..content_type_representation.content_type_serializer import ContentTypeSerializer


class ContextViewParamsSerializer(DynamicModelSerializer):
    table_type = DynamicRelationField(ContentTypeSerializer, label=_('TableTypes'))

    class Meta:
        name = 'contextviewparams'
        model = ContextViewParams
        fields = (
            'id',
            'table_type',
            'context',
            'view_params',
            'created',
            'updated',
        )
