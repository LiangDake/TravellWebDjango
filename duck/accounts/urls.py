from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),  # ''表示每一个操作
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]