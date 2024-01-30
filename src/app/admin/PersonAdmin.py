from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _

from app.models import Person


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    class Media:
        pass

    list_display = (
        'last_name',
        'birth_date',
        'birth_place',
    )
    search_fields = (
        'last_name',
    )
    readonly_fields = (
        'created',
        'updated',
    )
    fieldsets = (
        (
            _('personal data'),
            {
                'fields': (
                    'last_name',
                    'first_name',
                    'middle_name',
                    'birth_date',
                    'birth_place',
                )
            },
        ),
        (
            _('extra information'),
            {
                'fields': (
                    'created',
                    'updated',
                ),
            },
        ),
    )
