from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student,Employee,Staff,Teacher,Parents
from .serializer import StudentSerializer,EmployeeSerializer,StaffSerializer,TeacherSerializer,ParentsSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class StaffViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class ParentsViewSet(viewsets.ModelViewSet):
    serializer_class = ParentsSerializer
    queryset = Parents.objects.all()





