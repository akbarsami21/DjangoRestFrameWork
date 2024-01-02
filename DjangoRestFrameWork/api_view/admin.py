from django.contrib import admin
from api_view.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','section','course','advisor']
