from django.db import models

branches = (('CS' , 'CS'), ('EC', 'EC'), ('MECH', 'MECH'))

# Create your models here.
class StudentDetails(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    student_id = models.CharField(unique=True, blank= False, max_length=100)
    branch = models.CharField(choices = branches, max_length=20)
    name = models.CharField(max_length=60)
    phone = models.IntegerField(blank = False, unique = True)
    email = models.EmailField(max_length=254)
    address = models.TextField(max_length=254)
    photo = models.ImageField( null= True, blank= True)

    def __str__(self) -> str:
        return self.student_id

class StudentMarks(models.Model):
    admission = models.OneToOneField(StudentDetails, on_delete=models.CASCADE, primary_key=True, related_name='marks', to_field = 'id')
    SUB1 = models.IntegerField()
    SUB2 = models.IntegerField()
    SUB3 = models.IntegerField()

