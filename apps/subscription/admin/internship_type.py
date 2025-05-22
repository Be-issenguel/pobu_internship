from django.contrib import admin
from ..models.internship_type import InternshipType

@admin.register(InternshipType)
class InternshipTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'duration')
