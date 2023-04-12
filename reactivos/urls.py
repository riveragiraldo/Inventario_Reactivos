from django.urls import path
from .views import *
app_name='reactivos'

urlpatterns=[
    path('', index, name='index'),
    path('reactivos/<int:pk>', detalle_reactivo, name='detalle_reactivo'),
    path('reactivos/crear', crear_reactivo, name='crear_reactivo'),
]
