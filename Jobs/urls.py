from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'jobs'
urlpatterns = [
    path('', views.index, name='index'),
    path('jobs', views.jobs, name='job'),
    path('l_admin', views.l_admin, name='l_admin'),
    path('main', views.main, name='main'),
   
]