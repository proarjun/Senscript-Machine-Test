from django.shortcuts import render
from rest_framework import generics
from .models import StudentDetails
from .serializers import StudentDetailsSerializer

# Create your views here.

class StudentDetailList(generics.ListCreateAPIView):
    serializer_class = StudentDetailsSerializer
    queryset = StudentDetails.objects.all()
    search_fields = ['student_id', 'phone', 'email']


class StudentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailsSerializer
    queryset = StudentDetails.objects.all()