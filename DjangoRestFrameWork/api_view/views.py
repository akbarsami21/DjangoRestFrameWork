from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_view.serializer import StudentSerialzer
from api_view.models import Student

# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_create(request,pk=None):
    if request.method=='GET':
        id=pk
        if id is not None:
            std=Student.objects.get(roll=id)
            serializer=StudentSerialzer(std)
            return Response(serializer.data)
        std=Student.objects.all()
        serializer=StudentSerialzer(std,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=StudentSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data inserted successfully'})
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id=pk
        std=Student.objects.get(roll=id)
        serializer=StudentSerialzer(std,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'full data updated successfully'})
        return Response(serializer.errors)
    
    if request.method=='PATCH':
        id=pk
        std=Student.objects.get(roll=id)
        serializer=StudentSerialzer(std,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data updated successfully'})
        return Response(serializer.errors)
    
    if request.method=='DELETE':
        id=pk
        std=Student.objects.get(roll=id)
        std.delete()
        return Response({'msg': 'data deleted successfully'})
    


