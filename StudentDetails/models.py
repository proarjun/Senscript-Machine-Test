from django.db import models

branches = (('CS' , 'CS'), ('EC', 'EC'), ('MECH', 'MECH'))

# Create your models here.
class StudentDetails(models.Model):
    student_id = models.CharField(primary_key=True, blank= False, max_length=100)
    branch = models.CharField(choices = branches, max_length=20)
    name = models.CharField(max_length=60)
    phone = models.IntegerField(blank = False, unique = True)
    email = models.EmailField(max_length=254)
    address = models.TextField(max_length=254)
    photo = models.ImageField( null= True, blank= True)