#Archivo para definición de urls de las diferentes vistas o apis que interactuan el front con el back

from .views import *
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reactivos'

urlpatterns = [
    # Dir_Lab
    
    path('validateemailsol', PreSolDirLab.as_view(), name='pre_sol_dir_lab'),
    path('solicitudes/', SolDirLab.as_view(), name='sol_dir_lab'),

    # UniCLab
    path('UniCLab/', Index.as_view(), name='index'),#Página de incio del aplicativo
    path('UniCLab/categorias/<str:category>', Enlaces.as_view(), name='enlaces'),# Página categorías, cuando se accede desde un móvil
    
    # Reactivos
    path('UniCLab/reactivos/<int:pk>', detalle_reactivo, name='detalle_reactivo'),# Detalle de reactivo
    path('UniCLab/reactivos/crear/', crear_reactivo, name='crear_reactivo'),# Crear reactivos
    path('UniCLab/unidades/crear/', CrearUnidades.as_view(), name='crear_unidades'),# crear unidades
    path('UniCLab/estados/crear/', crear_estado, name='crear_estado'),# Crear Estados
    path('UniCLab/almacenamiento/crear_interno/', crear_almacenamiento_interno, name='crear_almacenamiento_interno'),# Crear almacenamiento interno
    path('UniCLab/almacenamiento/crear_clase/', crear_clase_almacenamiento, name='crear_clase_almacenamiento'),# Crear Clase de alamacenamiento
    path('UniCLab/reactivos/editar_reactivo/<int:pk>/', editar_reactivo, name='editar_reactivo'), # Editar Reactivos
    path('reactivos/eliminar_reactivo/<int:pk>/', eliminar_reactivo, name='eliminar_reactivo'), # Eliminar Reactivos
    path('reactivos/activar_reactivo/<int:pk>/', activar_reactivo, name='activar_reactivo'),# Activar Reactivos
    path('UniCLab/reactivos/listado_reactivos/', ReactivosListView.as_view(), name='listado_reactivos'),# Listado de reactivos

    # Inventarios
    path('UniCLab/facultades/crear/', crear_facultad, name='crear_facultad'),# Crear Facultad
    path('UniCLab/marcas/crear/', crear_marca, name='crear_marca'),# Crear Marca
    path('UniCLab/ubicaciones_almacen/crear/', crear_walmacen, name='crear_walmacen'),# Crear ubicaciones en el almacén 
    path('UniCLab/destinos/crear/', crear_destino, name='crear_destino'),# Crear destino
    path('UniCLab/ubicaciones/crear/', crear_ubicacion, name='crear_ubicacion'),# Crear Ubicación Asignatura
    path('UniCLab/responsables/crear/', crear_responsable, name='crear_responsable'),# Crear Responsables
    path('UniCLab/reactivos/registrar_salida/', registrar_salida, name='registrar_salida'),# Registrar Salidas
    path('UniCLab/reactivos/editar_salida/<int:pk>/', editar_salida, name='editar salida'),# Editar Salidas
    path('UniCLab/reactivos/registrar_entrada/', registrar_entrada, name='registrar_entrada'),# Registrar Entradas
    path('UniCLab/reactivos/editar_entrada/<int:pk>/', editar_entrada, name='editar_entrada'),# Editar Entradas
    path('reactivos/eliminar_entrada/<int:pk>/', eliminar_entrada, name='eliminar_entrada'),# Eliminar Enradas
    path('reactivos/eliminar_salida/<int:pk>/', eliminar_salida, name='eliminar_salida'),# Eliminar Salidas
    path('UniCLab/reactivos/inventario/', InventarioListView.as_view(), name='inventario'), # Ver Inventario
    path('UniCLab/reactivos/ocultar_reactivo/<int:pk>/', OcultarReactivoView.as_view(), name='ocultar_reactivo'), # Ocultar Reactivo
    path('UniCLab/reactivos/mostrar_reactivo/<int:pk>/', MostrarReactivoView.as_view(), name='mostrar_reactivo'), # Mostrar Reactivo
    path('UniCLab/reactivos/revisar_disponibilidad/<int:pk>/', RevisarDisponibilidadView.as_view(), name='revisar_disponibilidad'), # Revisar Disponibilidad de Reactivo
    path('UniCLab/reactivos/listado_entradas/', EntradasListView.as_view(), name='listado_entradas'), # Listado de Entradas
    path('UniCLab/reactivos/listado_salidas/', SalidasListView.as_view(), name='listado_salidas'), # Listado de salidas

    # Administrar
    path('UniCLab/administrar/configuraciones/', views.configuraciones, name='configuraciones'),# Página de configuraciones
    path('UniCLab/administrar/manuales/descargar_manual_usuario/', descargar_manual, name='descargar_manual'),# Genera vista de manual
    path('UniCLab/administrar/imagenes/logo_institucional/', logo_institucional, name='logo_institucional'),# Genera logo intitucional
    path('UniCLab/solicitudes/crear_tipo/', CrearTipoSolicitud.as_view(), name='crear_tipo_solicitud'),# Crear tipo de solicitud
    path('UniCLab/solicitudes/registrar_solicitud/', RegistrarSolicitud.as_view(), name='registrar_solicitud'),# Registrar solicitud
    path('UniCLab/solicitudes/listado_solicitudes/', SolicitudesListView.as_view(), name='listado_solicitudes'),# Listado de solicitudes
    path('UniCLab/solicitudes/estado_solicitud/<str:solicitud_code>/', estado_solicitud, name='estado_solicitud'),# Estado de solicitud
    path('UniCLab/solicitudes/responder_solicitud/<str:solicitud_code>/', responder_solicitud, name='responder_solicitud'),# Responder solicitud    
    path('UniCLab/administrar/listado_eventos/', EventosListView.as_view(), name='listado_eventos'), # LIstado de eventos
    # path('UniCLab/administrar/enviar_correo/', enviar_correo, name='enviar_correo'), # ENviar Correo Admin
    path('UniCLab/solicitudes/solicitudes_externas/', SolicitudesExternasListView.as_view(), name='listado_solicitudes_externas'),# Listado de solicitudes esternas
    path('UniCLab/solicitudes/eliminar_solicitud_externa/<str:solicitud_code>/', eliminar_solicitud_externa, name='eliminar_solicitud_externa'),# Eliminar solicitud externa
    path('UniCLab/solicitudes/solicitud_leida/<str:solicitud_code>/', solicitud_leida, name='solicitud_leida'),# Marcar solicitud como leída
    path('UniCLab/solicitudes/solicitud_no_leida/<str:solicitud_code>/', solicitud_no_leida, name='solicitud_no_leida'),# Marcar solicitud como no leída

    # Usuarios
    path('UniCLab/laboratorios/crear/', crear_laboratorio, name='crear_laboratorio'),# Crear Laboratorio
    path('UniCLab/usuarios/editar/<int:pk>/', editar_usuario, name='editar_usuario'), #Editar Usuarios
    path('usuarios/eliminar_usuario/<int:pk>/', eliminar_usuario, name='eliminar_usuario'), # Eliminar Usuarios
    path('usuarios/activar_usuario/<int:pk>/', activar_usuario, name='activar_usuario'), # Activar Usuarios
    path('UniCLab/usuarios/listar/', UsuariosListView.as_view(), name='listado_usuarios'), # Listado de usuarios
    path('UniCLab/roles/crear/', CrearRoles.as_view(), name='crear_roles'), # Crear Roles
    path('UniCLab/usuarios/crear/',login_required(CrearUsuario.as_view()),name='crear_usuarios'), # Crear Usuarios
    
    # Funcionales
    path('get-value/', get_value, name='get_value'), # Actualiza campos
    path('autocomplete/', autocomplete, name='autocomplete'),# Autompletar en entradas
    path('autocomplete_react/', AutocompleteReactivosAPI.as_view(), name='autocompletereactivos'),# Autompletar en inventario
    path('autocomplete_input/', AutocompleteReactivosInAPI.as_view(), name='autocompletereactivosin'),# Autompletar en listado de entradas
    path('autocomplete_output/', AutocompleteReactivosOutAPI.as_view(), name='autocompletereactivosout'),# Autompletar en listado de salidas
    path('autocomplete_out/', AutocompleteOutAPI.as_view(), name='autocomplete_out'), # Autocompletar en salidas
    path('autocomplete_user/', AutocompleteUserAPI.as_view(), name='autocomplete_user'), # Autocompletar en Usuarios
    path('autocomplete_manager/', autocomplete_manager, name='autocomplete_manager'), # Autocompletar responsables
    path('autocomplete_location/', autocomplete_location, name='autocomplete_location'), # Autocompletar Ubicaciones
    path('api/namesandtrademarksandreferencesbylab/', NamesTrademarksAndReferencesByLabAPI.as_view(), name='select-updatetrademarksandreferences'), # Actualiza nombres, marcas y refernecias por laboratorio
    path('api/in/selectoptionsbylab/', SelectOptionsByLabIN.as_view(), name='select-updatetrademarksandreferences'),# Actualiza selectores en listado de entradas
    path('api/out/selectoptionsbylab/', SelectOptionsByLabOUT.as_view(), name='select-updatetrademarksandreferences'),# Actualiza selectores en listado de salidas
    path('api/trademarksbylabandname/', TrademarksByLabAndNameAPI.as_view(), name='select-updatetrademarksandreferences'),# Actualiza Marcas y referencias , por nombre y laboratorio
    path('api/referencesbylabandname/', ReferencesByLabAndNameAPI.as_view(), name='select-updatetrademarksandreferencesbyname'),# Actualiza referencias , por nombre y laboratorio
    path('api/referencesbytrademark/', ReferencesByTrademarkAPI.as_view(), name='select-updatereferences'),# Actualiza referencias , por marca
    path('api/wlocations/', WlocationsAPI.as_view(), name='select-wlocations'), # Actualiza Ubicaciones en almacén según laboratorio  
    path('UniClab/captcha_refresh/', recargar_captcha, name='recargar_captcha'), # Actualizar Captcha
    # Exportar
    path('exportar-excel/', views.export_to_excel, name='export_to_excel'), # Exporta a Excel en Inventarios
    path('export2xlsxinput/', views.export_to_excel_input, name='export_to_excel_input'),# Exporta a Excel en Listado de Entradas
    path('export2xlsxoutput/', views.export_to_excel_output, name='export_to_excel_output'),# Exporta a Excel en Listado de Salidas
    path('export2xlsxreact/', views.export_to_excel_react, name='export_to_excel_react'),# Exporta a Excel en Listado de Reactivos
    path('export2xlsxlab/', views.export_to_excel_lab, name='export_to_excel_lab'),# Exporta a Excel en Listado de Laboratorios
    path('export2xlsxuser/', views.export_to_excel_user, name='export_to_excel_user'),# Exporta a Excel en Listado de Usuarios
    path('export2xlsxsolicitud/', views.export_to_excel_solicitud, name='export_to_excel_solicitud'),# Exporta a Excel en Listado de Solicitud
    path('export2xlsxsolicitudexterna/', views.export_to_excel_solicitud_externa, name='export_to_excel_solicitud_externa'),# Exporta a Excel en Listado de Solicitud
    path('export2xlsxevent/', views.export_to_excel_event, name='export_to_excel_event'),# Exporta a Excel en Listado de Eventos
    path('export_to_pdf/', views.export_to_pdf, name='export_to_pdf'),# Exporta a Pdf en Listado de Inventario
    
    # Paginaciones
    path('guardar-per-page/<int:per_page>/', GuardarPerPageView.as_view(), name='GuardarPerPage'),# Maneja paginación en Inventario
    path('guardar-per-page-event/<int:per_page>/', GuardarPerPageViewEvent.as_view(), name='GuardarPerPageEvent'),# Maneja paginación en listado de eventos
    path('guardar-per-page-in/<int:per_page>/', GuardarPerPageViewIn.as_view(), name='GuardarPerPageIn'),# Maneja paginación en listado de entradas
    path('guardar-per-page-out/<int:per_page>/', GuardarPerPageViewOut.as_view(), name='GuardarPerPageOut'),# Maneja paginación en listado de salidas
    path('guardar-per-page-reactivo/<int:per_page>/', GuardarPerPageViewReactivo.as_view(), name='GuardarPerPageReactivo'),# Maneja paginación en listado de reactivos
    path('guardar-per-page-user/<int:per_page>/', GuardarPerPageViewUser.as_view(), name='GuardarPerPageUser'),# Maneja paginación en listado de usuarios
    path('guardar-per-page-solicitud/<int:per_page>/', GuardarPerPageViewSolicitud.as_view(), name='GuardarPerPageSolicitud'),# Maneja paginación en listado de solicitudes
    path('guardar-per-page-solicitud-externa/<int:per_page>/', GuardarPerPageViewSolicitudExterna.as_view(), name='GuardarPerPageSolExterna'),# Maneja paginación en listado de solicitudes externas
    path("obtener_stock/", obtener_stock, name="obtener_stock"),# Obtiene el stock de un reactivo en registro de salidas
    path('check_auth_status/', check_auth_status, name='check_auth_status'),# Cerificar estado de autenticación

    # Transversales
    path('templates/webtemplate/', webtemplate, name='webtemplate'),# Visualiza WebTemplate
    path('UniCLab/accounts/login/', LoginView.as_view(), name='login'),# Login
    path("UniCLab/logout/", LogoutView.as_view(), name="logout"),# Logout
    path("UniCLab/password_change/", PasswordChangeView.as_view(), name="password_change"),# Cambiar Pass
    path("UniCLab/password_change/done/",PasswordChangeDoneView.as_view(),name="password_change_done_reactivos"),# Éxito de cambio de pass
    path("UniCLab/password_reset/", CustomPasswordResetView.as_view(), name="password_reset"), # REstablecer Pass
    path("UniCLab/password_reset/done/",PasswordResetDoneView.as_view(),name="password_reset_done_reactivos"), # Exito de restablecimiento de pass
    path("UniCLab/reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(),name="password_reset_confirmacion",),# Página de restablecimiento de la contraseña
    path("UniCLab/reset/done/",PasswordResetCompleteView.as_view(),name="password_reset_complete",),
    ]


