from django.contrib import admin
from django.urls import path,include
from blogs import views

urlpatterns = [
    path('', views.index,name='blogHome'),
    path('blogpost/', views.blogpost,name='blogPost'),
]
