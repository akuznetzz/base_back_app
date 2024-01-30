from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework.permissions import IsAuthenticated

from app.models import Person
from app.serializers import PersonSerializer


class PersonViewSet(DynamicModelViewSet):
    queryset = Person.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = PersonSerializer
