from typing import Any
from django.contrib import admin
from ..models.responsible import Responsible

@admin.register(Responsible)
class ResponsibleAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'phone', 'document', 'document_type')
    list_display = ('name', 'email', 'phone', 'document_type', 'document', 'user')
    list_display_links = ('user',)
    list_select_related = ('user',)


    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)