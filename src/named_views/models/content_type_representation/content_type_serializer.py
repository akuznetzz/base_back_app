from django.contrib.contenttypes.models import ContentType

from dynamic_rest.serializers import DynamicModelSerializer


class ContentTypeSerializer(DynamicModelSerializer):

    class Meta:
        model = ContentType
        name = 'contenttype'
        fields = (
            'id',
            'app_label',
            'model',
        )
