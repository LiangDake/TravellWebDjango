from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')  # ''表示每一个操作
]