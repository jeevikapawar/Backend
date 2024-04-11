from django.contrib import admin
from . models import *
from .models import Class, Student, AttendanceRecord

# Register your models here.
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(AttendanceRecord)