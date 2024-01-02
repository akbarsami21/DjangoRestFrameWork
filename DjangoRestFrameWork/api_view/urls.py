from django.urls import path
from api_view import views
urlpatterns = [
     path('info/', views.student_create), 
     path('info/<int:pk>', views.student_create), 
]