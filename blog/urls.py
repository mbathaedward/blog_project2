from django.contrib import admin
from django.urls import path
from . import views

#defining urls
urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('detail/<int:pk>/', views.post_detail, name='detail')
    
  
]