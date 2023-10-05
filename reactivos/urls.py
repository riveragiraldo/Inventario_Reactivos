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
    path('reactivos/editar_salida/<int:pk>/', editar_salida, name='editar salida'),
    path('reactivos/registrar_entrada/', registrar_entrada, name='registrar_entrada'),
    path('reactivos/editar_entrada/<int:pk>/', editar_entrada, name='editar_entrada'),
    path('usuarios/editar/<int:pk>/', EditarUsuario.as_view(), name='editar_usuario'),
    path('reactivos/editar_reactivo/<int:pk>/', editar_reactivo, name='editar_reactivo'),
    path('reactivos/eliminar_reactivo/<int:pk>/', eliminar_reactivo, name='eliminar_reactivo'),
    path('reactivos/activar_reactivo/<int:pk>/', activar_reactivo, name='activar_reactivo'),
    path('reactivos/eliminar_entrada/<int:pk>/', eliminar_entrada, name='eliminar_entrada'),
    path('reactivos/eliminar_salida/<int:pk>/', eliminar_salida, name='eliminar_salida'),
    path('reactivos/inventario/', InventarioListView.as_view(), name='inventario'),
    path('reactivos/listado_entradas/', EntradasListView.as_view(), name='listado_entradas'),
    path('reactivos/listado_salidas/', SalidasListView.as_view(), name='listado_salidas'),
    path('usuarios/listar/', UsuariosListView.as_view(), name='listado_usuarios'),
    path('reactivos/listado_reactivos/', ReactivosListView.as_view(), name='listado_reactivos'),
    path('roles/crear/', CrearRoles.as_view(), name='crear_roles'),
    path('usuarios/crear/',login_required(CrearUsuario.as_view()),name='crear_usuarios'),
    path('get-value/', get_value, name='get_value'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('autocomplete_out/', AutocompleteOutAPI.as_view(), name='autocomplete_out'),
    path('autocomplete_user/', AutocompleteUserAPI.as_view(), name='autocomplete_user'),
    path('autocomplete_manager/', autocomplete_manager, name='autocomplete_manager'),
    path('autocomplete_location/', autocomplete_location, name='autocomplete_location'),
    path('api/namesandtrademarksandreferencesbylab/', NamesTrademarksAndReferencesByLabAPI.as_view(), name='select-updatetrademarksandreferences'),
    path('api/in/selectoptionsbylab/', SelectOptionsByLabIN.as_view(), name='select-updatetrademarksandreferences'),
    path('api/out/selectoptionsbylab/', SelectOptionsByLabOUT.as_view(), name='select-updatetrademarksandreferences'),
    path('api/trademarksbylabandname/', TrademarksByLabAndNameAPI.as_view(), name='select-updatetrademarksandreferences'),
    path('api/referencesbylabandname/', ReferencesByLabAndNameAPI.as_view(), name='select-updatetrademarksandreferencesbyname'),
    path('api/referencesbytrademark/', ReferencesByTrademarkAPI.as_view(), name='select-updatereferences'),
    path('api/wlocations/', WlocationsAPI.as_view(), name='select-wlocations'),   
    path('exportar-excel/', views.export_to_excel, name='export_to_excel'),
    path('export2xlsxinput/', views.export_to_excel_input, name='export_to_excel_input'),
    path('export2xlsxoutput/', views.export_to_excel_output, name='export_to_excel_output'),
    path('export2xlsxreact/', views.export_to_excel_react, name='export_to_excel_react'),
    path('export2xlsxlab/', views.export_to_excel_lab, name='export_to_excel_lab'),
    path('export2xlsxuser/', views.export_to_excel_user, name='export_to_excel_user'),
    path('export_to_pdf/', views.export_to_pdf, name='export_to_pdf'),
    path('guardar-per-page/<int:per_page>/', GuardarPerPageView.as_view(), name='GuardarPerPage'),
    path('guardar-per-page-in/<int:per_page>/', GuardarPerPageViewIn.as_view(), name='GuardarPerPageIn'),
    path('guardar-per-page-out/<int:per_page>/', GuardarPerPageViewOut.as_view(), name='GuardarPerPageOut'),
    path('guardar-per-page-reactivo/<int:per_page>/', GuardarPerPageViewReactivo.as_view(), name='GuardarPerPageReactivo'),
    path('guardar-per-page-user/<int:per_page>/', GuardarPerPageViewUser.as_view(), name='GuardarPerPageUser'),
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
    
    
    ]


