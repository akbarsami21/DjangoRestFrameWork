from rest_framework import serializers
from . models import Teacher

# class TeacherSerializer(serializers.Serializer):
#     teacher_id=serializers.IntegerField()
#     name=serializers.CharField(max_length=100)
#     course=serializers.CharField(max_length=100)
#     seat=serializers.IntegerField()
#     duration=serializers.IntegerField()
    
#     def create(self,validated_data):
#         return Teacher.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         #instance = previous data save
#         #validated data = updated data handle 
#         instance.name=validated_data.get('name',instance.name)
#         instance.course=validated_data.get('course',instance.course)
#         instance.seat=validated_data.get('seat',instance.seat)
#         instance.duration=validated_data.get('duration',instance.duration)
#         instance.save()
#         return instance

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['teacher_id','name','course','seat','duration']

