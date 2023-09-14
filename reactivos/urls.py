#Archivo para definición de urls de las diferentes vistas o apis que interactuan el front con el back

from .views import *
from . import views
from django.urls import path, include

app_name = 'reactivos'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('reactivos/<int:pk>', detalle_reactivo, name='detalle_reactivo'),
    path('reactivos/crear/', crear_reactivo, name='crear_reactivo'),
    path('unidades/crear/', CrearUnidades.as_view(), name='crear_unidades'),
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
    path('reactivos/registrar_salida/', registrar_salida, name='registrar_salida'),
    path('reactivos/registrar_entrada/', registrar_entrada, name='registrar_entrada'),
    path('reactivos/inventario/', InventarioListView.as_view(), name='inventario'),
    path('reactivos/listado_entradas/', EntradasListView.as_view(), name='listado_entradas'),
    path('roles/crear/', CrearRoles.as_view(), name='crear_roles'),
    path('get-value/', get_value, name='get_value'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('autocomplete_out/', AutocompleteOutAPI.as_view(), name='autocomplete_out'),
    path('reactivos/registrar_salida/autocomplete_location/', autocomplete_location, name='autocomplete_location'),
    path('reactivos/registrar_salida/autocomplete_manager/', autocomplete_manager, name='autocomplete_manager'),
    path('reactivos/registrar_entrada/autocomplete_manager/', autocomplete_manager, name='autocomplete_manager'),
    path('reactivos/registrar_entrada/autocomplete_location/', autocomplete_location, name='autocomplete_location'),
    path('api/namesandtrademarksandreferencesbylab/', NamesTrademarksAndReferencesByLabAPI.as_view(), name='select-updatetrademarksandreferences'),
    path('api/selectoptionsbylab/', SelectOptionsByLabAPI.as_view(), name='select-updatetrademarksandreferences'),
    path('api/trademarksbylabandname/', TrademarksByLabAndNameAPI.as_view(), name='select-updatetrademarksandreferences'),
    path('api/referencesbylabandname/', ReferencesByLabAndNameAPI.as_view(), name='select-updatetrademarksandreferencesbyname'),
    path('api/referencesbytrademark/', ReferencesByTrademarkAPI.as_view(), name='select-updatereferences'),
    path('api/wlocations/', WlocationsAPI.as_view(), name='select-wlocations'),   
    path('exportar-excel/', views.export_to_excel, name='export_to_excel'),
    path('export2xlsxinput/', views.export_to_excel_input, name='export_to_excel_input'),
    path('export_to_pdf/', views.export_to_pdf, name='export_to_pdf'),
    path('guardar-per-page/<int:per_page>/', GuardarPerPageView.as_view(), name='GuardarPerPage'),
    path('guardar-per-page-in/<int:per_page>/', GuardarPerPageViewIn.as_view(), name='GuardarPerPageIn'),
    path("obtener_stock/", obtener_stock, name="obtener_stock"),
    path('templates/webtemplate/', webtemplate, name='webtemplate'),
    
    path('accounts/login/', LoginView.as_view(), name='login'),
    

    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "password_change/", PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done_reactivos"
    ),
    path("password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done_reactivos",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirmacion",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path('usuarios/listado/',login_required(ListadoUsuarios.as_view()),name='listado_usuarios'),
    path('usuarios/crear/',login_required(CrearUsuario.as_view()),name='crear_usuarios'),
    
    ]


