from django.urls import path
from .views import *
app_name='reactivos'

urlpatterns=[
    path('', index, name='index'),
    path('reactivos/<int:pk>', detalle_reactivo, name='detalle_reactivo'),
    path('reactivos/crear', crear_reactivo, name='crear_reactivo'),
    path('unidades/crear', crear_unidad, name='crear_unidad'),
    path('marcas/crear', crear_marca, name='crear_marca'),
    path('destinos/crear', crear_destino, name='crear_destino'),
    path('asignaturas/crear', crear_asignatura, name='crear_asignatura'),
    path('asignaturas/crear', crear_asignatura, name='crear_ubicacion'),
    path('responsables/crear', crear_responsable, name='crear_responsable'),
    path('reactivos/registrar_salida', registrar_salida, name='registrar_salida'),
    path('get-value/', get_value, name='get_value'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    
]
