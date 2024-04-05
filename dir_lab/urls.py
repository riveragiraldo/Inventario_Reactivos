#Archivo para definición de urls de las diferentes vistas o apis que interactuan el front con el back

from .views import *
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dir_lab'

urlpatterns = [
    # Dir_Lab
    path('', HomeDirLab.as_view(), name='home_dir_lab'),#Página de incio del aplicativo
    
    ]


