from django.urls import path,include
from classapiview import views
from rest_framework.routers import DefaultRouter

#create router object
router=DefaultRouter()
#register router
router.register('info',views.EmpInfoViewSet,basename='viewset')
urlpatterns = [
     # path('info/', views.EmployeeInfo.as_view(),name='empall'), 
     # path('info/<int:pk>',views.EmployeeInfo.as_view(),name='empid'), 
    
     # path('data/',views.EmployeeData.as_view(),name='empdata'),
     # path('data/<int:pk>',views.EmployeeData.as_view()),
    
     # path('info/',views.EmployeCreate.as_view(),name='create'),
     # path('info/<int:pk>',views.EmployeUpdateDelete.as_view()),
      
]