from rest_framework import serializers
from .models import Student, Employee,Staff,Teacher,Parents


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = "__all__"
