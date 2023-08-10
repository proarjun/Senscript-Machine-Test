from django.db import models

branches = ('CS', 'EC', 'MECH')

# Create your models here.
class StudentDetails(models.Model):
    student_id = models.CharField(primary_key=True, default="STD_", blank= False)
    branch = models.Choices