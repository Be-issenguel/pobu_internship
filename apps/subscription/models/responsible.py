from django.db import models
from ..choices import DOCUMENT_TYPE_CHOICES


class Responsible(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    document = models.CharField(max_length=14)
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='responsibles')

    def __str__(self):
        return f"#{self.id} . {self.name}"