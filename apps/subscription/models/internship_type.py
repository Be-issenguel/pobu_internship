from django.db import models


class InternshipType(models.Model):
    type = models.CharField(max_length=40)
    duration = models.IntegerField(help_text="duration of the internship")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
