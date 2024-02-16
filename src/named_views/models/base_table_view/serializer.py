from django.utils.translation import gettext_lazy as _
from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField

from .model import BaseTableView
from ..content_type_representation.content_type_serializer import ContentTypeSerializer


class BaseTableViewSerializer(DynamicModelSerializer):
    table_type = DynamicRelationField(ContentTypeSerializer, label=_('TableTypes'))

    class Meta:
        name = 'basetableview'
        model = BaseTableView
        fields = (
            'id',
            'table_type',
            'view_text',
            'context',
            'created',
            'updated',
        )
