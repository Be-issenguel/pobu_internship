from django.db import models
from .student import Student
from .internship_type import InternshipType


class Internship(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='internships')
    internship_type = models.ForeignKey(InternshipType, on_delete=models.CASCADE)
