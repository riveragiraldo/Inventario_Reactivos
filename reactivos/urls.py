#Archivo para definición de urls de las diferentes vistas o apis que interactuan el front con el back

from django.urls import path
from .views import *
from . import views
app_name = 'reactivos'

urlpatterns = [
    path('', index, name='index'),
    path('reactivos/<int:pk>', detalle_reactivo, name='detalle_reactivo'),
    path('reactivos/crear/', crear_reactivo, name='crear_reactivo'),
    path('unidades/crear/', crear_unidades, name='crear_unidades'),
    path('estados/crear/', crear_estado, name='crear_estado'),
    path('facultades/crear/', crear_facultad, name='crear_facultad'),
    path('laboratorios/crear/', crear_laboratorio, name='crear_laboratorio'),
    path('marcas/crear/', crear_marca, name='crear_marca'),
    path('ubicaciones_almacen/crear/', crear_walmacen, name='crear_walmacen'),
    path('respel/crear/', crear_respel, name='crear_respel'),
    path('sga/crear/', crear_sga, name='crear_sga'),
    path('destinos/crear/', crear_destino, name='crear_destino'),
    path('ubicaciones/crear/', crear_ubicacion, name='crear_ubicacion'),
    path('responsables/crear/', crear_responsable, name='crear_responsable'),
    path('reactivos/registrar_salida/',
         registrar_salida, name='registrar_salida'),
    path('reactivos/registrar_entrada/', registrar_entrada, name='registrar_entrada'),
    path('reactivos/inventario/', InventarioListView.as_view(), name='inventario'),
    path('get-value/', get_value, name='get_value'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('autocomplete_out/', AutocompleteOutAPI.as_view(), name='autocomplete_out'),
    path('reactivos/registrar_salida/autocomplete_location/',
         autocomplete_location, name='autocomplete_location'),
    path('reactivos/registrar_salida/autocomplete_manager/',
         autocomplete_manager, name='autocomplete_manager'),
    path('reactivos/registrar_entrada/autocomplete_manager/',
         autocomplete_manager, name='autocomplete_manager'),
    path('reactivos/registrar_entrada/autocomplete_location/',
         autocomplete_location, name='autocomplete_location'),
    path('api/trademarks/', TrademarksAPI.as_view(), name='select-trademarks'),
    path('api/reactives/', ReactivesAPI.as_view(), name='select-reactives'),
    path('api/references/', ReferencesAPI.as_view(), name='select-references'),
    path('api/wlocations/', WlocationsAPI.as_view(), name='select-wlocations'),   
    path('exportar-excel/', views.export_to_excel, name='export_to_excel'),
    path('export_to_pdf/', views.export_to_pdf, name='export_to_pdf'),
    path('guardar-per-page/<int:per_page>/', GuardarPerPageView.as_view(), name='GuardarPerPage'),
    path("obtener_stock/", obtener_stock, name="obtener_stock"),

]
