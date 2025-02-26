from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student,Employee,Staff,Teacher,Parents
from .serializer import StudentSerializer,EmployeeSerializer,StaffSerializer,TeacherSerializer,ParentsSerializer

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class ParentsViewSet(viewsets.ModelViewSet):
    serializer_class = ParentsSerializer
    queryset = Parents.objects.all()





