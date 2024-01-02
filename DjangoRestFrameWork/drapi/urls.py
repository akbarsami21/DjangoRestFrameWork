from django.urls import path
from drapi import views
urlpatterns = [
     path('info/',views.teacherinfoall ),
     path('bypk/<int:pk>',views.teacherinfobypk ),
     path('register/',views.teacher_create,name="teacher" ),
]
