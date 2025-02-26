from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    mob=models.IntegerField()
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    mob=models.IntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    mob=models.IntegerField()

    def __str__(self):
        return self.name
    
class Parents(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    mob=models.IntegerField()
    def __str__(self):
        return self.name