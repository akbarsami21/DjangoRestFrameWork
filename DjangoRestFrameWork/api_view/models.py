from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    roll=models.IntegerField()
    section=models.CharField(max_length=10)
    course=models.CharField(max_length=50)
    advisor=models.CharField(max_length=200)
