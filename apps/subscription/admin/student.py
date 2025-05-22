from django.contrib import admin
from ..models.student import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'grade', 'document', 'document_type', 'school')
    list_filter = ('school',)
