from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework import status
from rest_framework import views
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.model_name_to_entity_name import get_entity_name
from app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        name = 'user'
        model = User
        fields = (
            'id',
            'email',
            'is_staff',
            'is_active',
            'person',
            'person_id',
            'permissions'
        )

    person = SerializerMethodField(label=_('persons'))
    permissions = SerializerMethodField(label=_('permissions'))

    @staticmethod
    def get_person(obj):
        return str(obj.person) if obj.person else ''

    @staticmethod
    def get_permissions(user: User):
        result = {}
        for full_permission in user.get_all_permissions():
            app, permission = full_permission.split('.')
            if app == 'flow':  # skipping flow for now
                continue
            operation, model_name = permission.split('_')
            entity_name = get_entity_name(app, model_name)
            # just skipping models without corresponding entity name, i.e. models that are not registered in router
            if entity_name is not None:
                operations = result.setdefault(entity_name, set())
                assert operation not in operations
                operations.add(operation)
        return result

class MeView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
