from rest_framework import serializers
from classapiview.models import Employee

class EmployeeSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['id','name','eid','advisor']