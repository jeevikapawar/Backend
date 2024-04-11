from django.db import models
from django.contrib.auth.models import User



# Create your models here.
''''
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)'''
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other teacher fields as needed
class Class(models.Model):
    name = models.CharField(max_length=100)
    
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    RollNumber = models.BigIntegerField(default=0)
    Degree = models.CharField(max_length=30)
    Major = models.CharField(max_length=64)
    
#Attendance
class AttendanceRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_attended = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField() #true for Present. False for Absent.


