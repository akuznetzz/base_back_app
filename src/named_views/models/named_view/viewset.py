from dynamic_rest.viewsets import DynamicModelViewSet
from .model import NamedView
from .serializer import NamedViewSerializer


class NamedViewViewSet(DynamicModelViewSet):
    queryset = NamedView.objects.all()
    serializer_class = NamedViewSerializer
