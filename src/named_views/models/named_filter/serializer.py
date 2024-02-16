from copy import copy

from django.utils.translation import gettext_lazy as _
from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from rest_framework import validators

from app.serializers.UserSerializer import UserSerializer
from .model import NamedFilter
from ..content_type_representation.content_type_serializer import ContentTypeSerializer


class NamedFilterSerializer(DynamicModelSerializer):
    user = DynamicRelationField(
        UserSerializer,
        label=_('user'),
    )
    table_type = DynamicRelationField(ContentTypeSerializer, label=_('TableTypes'))

    class Meta:
        name = 'namedfilter'
        model = NamedFilter
        fields = (
            'id',
            'user',
            'table_type',
            'context',
            'name',
            'view_text',
            'created',
            'updated',
        )

    def run_validators(self, value):
        for validator in copy(self.validators):
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super().run_validators(value)
