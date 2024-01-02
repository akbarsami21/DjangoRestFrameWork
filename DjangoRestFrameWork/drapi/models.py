from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id=models.IntegerField()
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    seat=models.IntegerField()
    duration=models.IntegerField()
