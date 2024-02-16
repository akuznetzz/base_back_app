from dynamic_rest.viewsets import DynamicModelViewSet

from .model import ContextViewParams
from .serializer import ContextViewParamsSerializer


class ContextViewParamsViewSet(DynamicModelViewSet):
    queryset = ContextViewParams.objects.all()
    serializer_class = ContextViewParamsSerializer
