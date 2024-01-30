
from dynamic_rest.serializers import DynamicModelSerializer

from app.models import Person


class PersonSerializer(DynamicModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'last_name',
            'first_name',
            'middle_name',
            'birth_date',
            'birth_place',
        )
        plural_name = 'persons'
