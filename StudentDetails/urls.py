from django.urls import path
from .views import StudentDetailList, StudentView, StudentMarksList, StudentMarksView

urlpatterns = [
    path('', StudentDetailList.as_view(), name='student_detail_list'),
    path('<int:pk>', StudentView.as_view(), name='student_view'),
    path('marks/<int:pk>', StudentMarksList.as_view(), name='student_marks_list'),
    path('marks/<int:pk>/update', StudentMarksView.as_view(), name='student_marks_view'),
]