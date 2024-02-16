
from dynamic_rest.serializers import DynamicModelSerializer

from app.models import User


class UserSerializer(DynamicModelSerializer):
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
        )
