from django.urls import path
from .views import *
app_name='reactivos'

urlpatterns=[
    path('', index, name='index'),
    path('reactivos/<int:pk>', detalle_reactivo, name='detalle_reactivo'),
    path('reactivos/crear/', crear_reactivo, name='crear_reactivo'),
    path('reactivos/crear_confirm/', crear_reactivo_confirm, name='crear_reactivo_confirm'),
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
    path('reactivos/registrar_salida_confirm/', registrar_salida_confirm, name='registrar_salida_confirm'),
    path('reactivos/registrar_entrada/', registrar_entrada, name='registrar_entrada'),
    path('reactivos/registrar_entrada_confirm/', registrar_entrada_confirm, name='registrar_entrada_confirm'),
    path('reactivos/inventario/', InventarioListView.as_view(), name='inventario'),
    path('get-value/', get_value, name='get_value'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('reactivos/registrar_salida/autocomplete_location/', autocomplete_location, name='autocomplete_location'),
    path('reactivos/registrar_salida/autocomplete_manager/', autocomplete_manager, name='autocomplete_manager'),
    path('reactivos/registrar_entrada/autocomplete_manager/', autocomplete_manager, name='autocomplete_manager'),
     path('reactivos/registrar_entrada/autocomplete_location/', autocomplete_location, name='autocomplete_location'),
    
]
