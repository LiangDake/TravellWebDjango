from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'), # ''表示每一个操作
    path('add', views.add, name='add')
]