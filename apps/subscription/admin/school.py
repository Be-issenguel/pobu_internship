from typing import Any
from django.contrib import admin
from ..models.school import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    fields = ('name', 'number', 'responsible')
    list_display = ('name', 'number', 'responsible', 'user')
    search_fields = ('name', )

    def save_model(self, request, obj, form, change) -> None:
        if not obj.pk:
            obj.user = request.user
        return super().save_model(request, obj, form, change)
