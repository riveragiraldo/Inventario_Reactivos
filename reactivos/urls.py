from django.urls import path
from .views import *
app_name='reactivos'

urlpatterns=[
    path('', index, name='index'),
    path('reactivos/<int:pk>', detalle_reactivo, name='detalle_reactivo'),
    path('reactivos/crear/', crear_reactivo, name='crear_reactivo'),
    path('unidades/crear/', crear_unidad, name='crear_unidad'),
    path('unidades/creacion/', crear_unidades, name='crear_unidades'),
    path('marcas/crear/', crear_marca, name='crear_marca'),
    path('marcas/creacion/', crear_marcas, name='crear_marcas'),
    path('destinos/creacion/', crear_destinos, name='crear_destinos'),
    path('destinos/crear/', crear_destino, name='crear_destino'),
    path('ubicaciones/crear/', crear_ubicacion, name='crear_ubicacion'),
    path('ubicaciones/creacion/', crear_ubicaciones, name='crear_ubicaciones'),
    path('responsables/crear/', crear_responsable, name='crear_responsable'),
    path('reactivos/registrar_salida/', registrar_salida, name='registrar_salida'),
    path('get-value/', get_value, name='get_value'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('reactivos/autocomplete_location/', autocomplete_location, name='autocomplete_location'),
    path('reactivos/autocomplete_manager/', autocomplete_manager, name='autocomplete_manager'),
    
]
