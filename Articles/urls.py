from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('detail/<int:g_pk>', views.detail),
    path('delete/<int:g_pk>', views.delete),
    path('fix/<int:g_pk>', views.fix),
    path('edit/<int:g_pk>', views.edit),
    path('delete_all', views.delete_all),
]
