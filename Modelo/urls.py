from django.urls import path, re_path
from django.conf.urls import include 
from django.contrib.auth.models import User

from Modelo import views

urlpatterns = [
    re_path(r'registro_lista/$', views.RegistroList.as_view()),
]