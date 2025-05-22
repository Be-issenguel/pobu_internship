from django.db import models
from .school import School
from ..choices import DOCUMENT_TYPE_CHOICES


class Student(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    grade = models.CharField(max_length=10)
    document = models.CharField(max_length=14)
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPE_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schools')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='schools')
