from django.urls import path
from . import views


urlpatterns = [

 path('',views.gallery,name='gallery'),
    
  path('add_photo/',views.addPhoto,name='add_photo'),
    
  path('photo/<str:pk>',views.viewPhoto,name='photo'),
  
]