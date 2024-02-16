from django.contrib.admin import ModelAdmin
from .model import NamedView


class NamedViewAdmin(ModelAdmin):
    model = NamedView
    list_display = ('id', 'user', 'table_type', 'name', 'context', 'view_text',  'created', 'updated',)
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
                    'name',
                    'context',
                    'view_text',
                    'created',
                    'updated',
                )
            }
        ),
    )

    def __str__(self):
        return f'{str(self.name)}'
