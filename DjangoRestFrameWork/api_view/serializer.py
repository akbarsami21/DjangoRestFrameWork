from rest_framework import serializers
from . models import Student

class StudentSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','roll','section','course','advisor']
    