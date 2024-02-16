from dynamic_rest.viewsets import DynamicModelViewSet

from .model import BaseTableView
from .serializer import BaseTableViewSerializer


class BaseTableViewViewSet(DynamicModelViewSet):
    queryset = BaseTableView.objects.all()
    serializer_class = BaseTableViewSerializer
