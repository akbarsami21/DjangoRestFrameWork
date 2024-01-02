from django.http import HttpResponse
from django.shortcuts import render
from drapi.serializer import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from drapi.models import Teacher
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.
#query set
#applicaiton of serializer
def teacherinfoall(request):
    cd=Teacher.objects.all()
    #python dict
    serializer=TeacherSerializer(cd,many=True)
    #convert in json
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

#applicaiton of serializer
def teacherinfobypk(request,pk):
    cd=Teacher.objects.get(id=pk)
    #python dict
    serializer=TeacherSerializer(cd)
    #convert in json
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

#applicaiton of deserializer
@csrf_exempt
def teacher_create(request):
    if request.method=='POST':
        #fetch the data from form
        json_data=request.body
        #convert into stream, mane bag bag kore data patai
        stream=io.BytesIO(json_data)
        #stream to python data
        python_data=JSONParser().parse(stream)
        #python to complex
        serializer=TeacherSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'successfully inserted the data'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('teacher_id')
        teacher=Teacher.objects.get(teacher_id=id)
        serializer=TeacherSerializer(teacher,data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'successfully updated the data'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('teacher_id')
        teacher=Teacher.objects.get(teacher_id=id)
        teacher.delete()
        res={'msg':'data deleted successfully'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
        
        




