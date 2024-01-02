from django.contrib import admin
from drapi.models import Teacher

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['teacher_id','name','course','seat','duration']
