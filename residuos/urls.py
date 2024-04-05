#Archivo para definición de urls de las diferentes vistas o apis que interactuan el front con el back

from .views import *
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'residuos'

urlpatterns = [
    # UniCLab Residuos
    path('UniCLab_Residuos/', HomeUniCLabResiduos.as_view(), name='home_residuos'),# Página de incio del aplicativo residuos
    
    ]


