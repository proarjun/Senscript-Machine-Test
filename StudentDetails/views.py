from django.shortcuts import render
from rest_framework import generics
from .models import StudentDetails, StudentMarks
from .serializers import StudentDetailsSerializer, StudentMarksSerializer

# Create your views here.

class StudentDetailList(generics.ListCreateAPIView):
    serializer_class = StudentDetailsSerializer
    queryset = StudentDetails.objects.all()
    search_fields = ['student_id', 'phone', 'email']


class StudentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailsSerializer
    queryset = StudentDetails.objects.all()

class StudentMarksList(generics.CreateAPIView, generics.RetrieveAPIView):
    serializer_class = StudentMarksSerializer
    queryset = StudentMarks.objects.all()

class StudentMarksView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentMarksSerializer
    queryset = StudentMarks.objects.all()