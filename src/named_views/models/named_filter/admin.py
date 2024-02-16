from django.contrib.admin import ModelAdmin

from .model import NamedFilter


class NamedFilterAdmin(ModelAdmin):
    model = NamedFilter
    list_display = (
        'id',
        'user',
        'table_type',
        'name',
        'view_text',
        'created',
        'updated',
    )
    readonly_fields = [
        'id',
        'created',
        'updated',
    ]
    fieldsets = (
        (
            '',
            {
                'fields': (
                    'id',
                    'user',
                    'table_type',
                    'context',
                    'name',
                    'view_text',
                    'created',
                    'updated',
                )
            },
        ),
    )

    def __str__(self):
        return f'{str(self.name)}'
