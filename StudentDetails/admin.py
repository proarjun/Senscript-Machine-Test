from django.contrib import admin
from .models import StudentDetails, StudentMarks

# Register your models here.

#admin.site.register(StudentDetails)
#admin.site.register(StudentMarks)

@admin.register(StudentDetails)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'branch', 'name', 'phone', 'email', 'address', 'photo']


@admin.register(StudentMarks)
class StudentMarksAdmin(admin.ModelAdmin):
    list_display = ['admission', 'SUB1', 'SUB2', 'SUB3']
