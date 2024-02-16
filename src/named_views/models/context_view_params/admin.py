from django.contrib.admin import ModelAdmin

from .model import ContextViewParams


class ContextViewParamsAdmin(ModelAdmin):
    model = ContextViewParams
    list_display = (
        'id',
        'table_type',
        'context',
        'view_params',
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
                    'table_type',
                    'context',
                    'view_params',
                    'created',
                    'updated',
                )
            },
        ),
    )

    def __str__(self):
        return f'{str(self.id)} for {str(self.table_type)} with context "{str(self.context)}"'
