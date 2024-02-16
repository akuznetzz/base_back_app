from dynamic_rest.viewsets import DynamicModelViewSet

from .model import NamedFilter
from .serializer import NamedFilterSerializer


class NamedFilterViewSet(DynamicModelViewSet):
    queryset = NamedFilter.objects.all()
    serializer_class = NamedFilterSerializer
