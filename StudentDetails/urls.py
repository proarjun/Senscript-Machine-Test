from django.urls import path
from .views import StudentDetailList, StudentView

urlpatterns = [
    path('', StudentDetailList.as_view(), name='student_detail_list'),
    path('<int:pk>', StudentView.as_view(), name='student_view'),
]