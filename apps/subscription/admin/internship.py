from django.contrib import admin
from ..models.internship import Internship

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'student', 'internship_type',)
