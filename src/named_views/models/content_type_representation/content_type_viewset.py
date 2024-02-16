from django.contrib.contenttypes.models import ContentType
from dynamic_rest.viewsets import DynamicModelViewSet

from named_views.models.content_type_representation.content_type_serializer import ContentTypeSerializer


class ContentTypeViewSet(DynamicModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
