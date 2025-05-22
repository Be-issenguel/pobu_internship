from django.db import models
from .responsible import Responsible

class School(models.Model):
    name = models.CharField(max_length=45)
    number = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    responsible = models.OneToOneField(Responsible, on_delete=models.CASCADE, related_name='school')

    def __str__(self):
        return f"{self.responsible}'s school"
