'''from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from classapiview.serializer import EmployeeSeralizer
from classapiview.models import Employee'''

# Create your views here.
"""""
class EmployeeInfo(APIView):
    def post(self,request,format=None):
        serializer=EmployeeSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data inserted'})
        return Response(serializer.errors)
    
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            emp=Employee.objects.get(eid=id)
            serializer=EmployeeSeralizer(emp)
            return Response(serializer.data)
        emp=Employee.objects.all()
        serializer=EmployeeSeralizer(emp,many=True)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        id=pk
        emp=Employee.objects.get(eid=id)
        serializer=EmployeeSeralizer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated succesffully'})
        return Response(serializer.errors)
        
    def patch(self,request,pk,format=None):
        id=pk
        emp=Employee.objects.get(eid=id)
        serializer=EmployeeSeralizer(emp,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated succesffully'})
        return Response(serializer.errors)
        
    def delete(self,request,pk,format=None):
        id=pk
        emp=Employee.objects.get(eid=id)
        emp.delete()
        return Response({'msg':'data deleted'}) """

'''
from .models import Employee
from .serializer import EmployeeSeralizer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class EmployeeData(GenericAPIView,ListModelMixin,CreateModelMixin,
                   RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSeralizer

    def get(self,request,*args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request,*args, **kwargs)
        else:
            return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)'''


'''
from classapiview.models import Employee
from classapiview.serializer import EmployeeSeralizer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class EmployeCreate(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSeralizer

class EmployeUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSeralizer'''

from rest_framework import viewsets
from classapiview.serializer import EmployeeSeralizer
from classapiview.models import Employee
from rest_framework.permissions import IsAdminUser

class EmpInfoViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSeralizer
    permission_classes=[IsAdminUser]

    
    
    

            
        

