# En este archivo se configuran las opciones de administración de Django

from django.contrib import admin
from .models import *
from django.views.generic import TemplateView
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .forms import CustomAuthenticationForm
from django.contrib.auth.models import Group, Permission
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Inclusión de creación de nuevos permisos en el admin de Dajango


@admin.register(Permission)
class Permisosadmin(admin.ModelAdmin):
    list_display=('id','name','content_type', 'codename')
    ordering=('id',)


# Inclusión de creación de nuevos Roles en el admin de Dajango
@admin.register(Rol)
class Rolesmin(admin.ModelAdmin):
    list_display=('id','name','date_created', 'user_create','last_update','last_updated_by',)
    ordering=('id',)

class UnidadesResources(resources.ModelResource):
    class Meta:
        model = Unidades


# Inclusión de el modelo UNIDADES en la consola de administración de Django
@admin.register(Unidades)
class Unidadesadmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','name','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)
    resource_class = UnidadesResources

# Inclusión de el modelo TIPOSOLICITUD en la consola de administración de Django
@admin.register(TipoSolicitud)
class TipoSolicitudadmin(admin.ModelAdmin):
    list_display=('id','name','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)

# Inclusión de el modelo SOLICITUDES en la consola de administración de Django
@admin.register(Solicitudes)
class Solicitudadmin(admin.ModelAdmin):
    list_display=('id','tipo_solicitud','name','tramitado','observaciones','archivos_adjuntos','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)

# Inclusión de el modelo Configuración del sistema en la consola de administración de Django
@admin.register(ConfiguracionSistema)
class Configuraciónadmin(admin.ModelAdmin):
    list_display=('id','tiempo_solicitudes','tiempo_eventos','correo_administrador','url')
    ordering=('id',)


class MarcasResources(resources.ModelResource):
    class Meta:
        model = Marcas

# Inclusión de el modelo MARCAS en la consola de administración de Django  
@admin.register(Marcas)
class Marcasadmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('id','name','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)
    resource_class = MarcasResources

# Inclusión de el modelo DESTINOS en la consola de administración de Django    
@admin.register(Destinos)
class Destinoadmin(admin.ModelAdmin):
    list_display=('id','name','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)


class EstadosResources(resources.ModelResource):
    class Meta:
        model = Estados


# Inclusión de el modelo ESTADOS en la consola de administración de Django
@admin.register(Estados)
class Estadoadmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','name','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)
    resource_class = EstadosResources

# Inclusión de el modelo UBICACIONES en la consola de administración de Django
@admin.register(Ubicaciones)
class Ubicacionadmin(admin.ModelAdmin):
    list_display=('id','name','facultad','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)

# Inclusión de el modelo FACULTADES en la consola de administración de Django
@admin.register(Facultades)
class Facultadadmin(admin.ModelAdmin):
    list_display=('id','name','created_by', 'date_create','last_update','last_updated_by')
    ordering=('id',)

class AlmacenamientoInternoResources(resources.ModelResource):
    class Meta:
        model = AlmacenamientoInterno

# Inclusión de el modelo ALMACENAMIENTO INTERNO en la consola de administración de Django
@admin.register(AlmacenamientoInterno)
class AlmacenamientoInternoadmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','name','description','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)
    resource_class = AlmacenamientoInternoResources

class ClaseAlmacenamientoResources(resources.ModelResource):
    class Meta:
        model = ClaseAlmacenamiento

# Inclusión de el modelo Clase Alamcenamietno en la consola de administración de Django
@admin.register(ClaseAlmacenamiento)
class ClaseAlmacenamientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','name','description','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)
    resource_class = ClaseAlmacenamientoResources

class LaboratoriosResources(resources.ModelResource):
    class Meta:
        model = Laboratorios    

# Inclusión de el modelo LABORATORIOS en la consola de administración de Django
@admin.register(Laboratorios)
class Laboratorioadmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','name','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)
    resource_class = LaboratoriosResources

# Inclusión de el modelo RESPONSABLES en la consola de administración de Django
@admin.register(Responsables)
class Responsableadmin(admin.ModelAdmin):
    list_display=('id','name','mail','phone','is_active','cc','acceptDataProcessing','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)


class AlmacenamientoResources(resources.ModelResource):
    class Meta:
        model = Almacenamiento


# Inclusión de el modelo ALMACENAMIENTO en la consola de administración de Django
@admin.register(Almacenamiento)
class Almacenamientoadmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','lab','name','description','created_by', 'date_create','last_update','last_updated_by',)
    ordering=('id',)
    resource_class = AlmacenamientoResources

class ReactivosResources(resources.ModelResource):
    class Meta:
        model = Reactivos


# Inclusión de el modelo REACTIVOS en la consola de administración de Django
@admin.register(Reactivos)
class Reactivosadmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','code','cas','name','state','unit','almacenamiento_interno','clase_almacenamiento','created_by', 'date_create','last_update','last_updated_by',)
    list_filter=('code','name',)
    search_fields=('code','name',)
    list_per_page=10
    ordering=('id',)
    resource_class = ReactivosResources

class TipoEventoResources(resources.ModelResource):
    class Meta:
        model = TipoEvento


# Inclusión de el modelo TIPO DE EVENTO en la consola de administración de Django
@admin.register(TipoEvento)
class TipoEventoadmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('name','id',)
    list_filter=('id','name',)
    search_fields=('name',)
    list_per_page=20
    ordering=('id',)
    resource_class = TipoEventoResources

# Inclusión de el modelo EVENTOS en la consola de administración de Django
@admin.register(Eventos)
class Eventoadmin(admin.ModelAdmin):
    list_display = ('tipo_evento', 'id', 'display_usuario_evento', 'fecha_evento',)
    list_filter = ('tipo_evento', 'usuario_evento',)
    search_fields = ('tipo_evento', 'usuario_evento',)
    list_per_page = 20
    ordering = ('-fecha_evento',)

    def display_usuario_evento(self, obj):
        # Personaliza cómo se muestra usuario_evento en la lista
        return f"{obj.usuario_evento.first_name} {obj.usuario_evento.last_name}"
    
    display_usuario_evento.short_description = 'Usuario del Evento'  # Cambia el encabezado de la columna

    def get_queryset(self, request):
        # Optimiza la consulta para reducir la carga de la base de datos
        return super().get_queryset(request).select_related('usuario_evento')



# Inclusión de el modelo ENTRADAS en la consola de administración de Django
@admin.register(Entradas)
class Entradaadmin(admin.ModelAdmin):
    list_display=('id','is_active','name','created_by', 'date_create','last_updated_by','last_update','trademark','reference','weight','order','date_order','manager','observations','location','price','nproject','destination','lab','observations', )
    list_filter=('date_create','name','lab',)
    search_fields=('date_create','name','lab',)
    list_per_page=10
    ordering=('id',)

# Inclusión de el modelo SALIDAS en la consola de administración de Django
@admin.register(Salidas)
class Salidaadmin(admin.ModelAdmin):
    list_display=('id','name','trademark','reference','weight','destination','manager','observations','location','lab','created_by', 'date_create','last_update','last_updated_by',)
    list_filter=('name','lab')
    search_fields=('name','lab')
    list_per_page=10
    ordering=('id',)

# Inclusión de el modelo INVENTARIOS en la consola de administración de Django
@admin.register(Inventarios)
class Inventarioadmin(admin.ModelAdmin):
    list_display=('id','name','is_active','trademark','weight','reference','lab','wlocation','minStockControl','minstock','edate','created_by', 'date_create','last_update','last_updated_by',)
    list_filter=('trademark','name','reference','lab',)
    search_fields=('trademark','name','reference','lab',)
    list_per_page=10
    ordering=('id',)



class UserAdmin(BaseUserAdmin):
    # Especifica los campos a mostrar en la lista de usuarios en el admin
    list_display = ('id','first_name', 'last_name','acceptDataProcessing','rol','email', 'lab','is_active','user_create', 'date_joined','last_update','last_updated_by','id_number','phone_number',)
    list_editable = ['first_name', 'last_name','email','lab', 'rol',]
    ordering=('id',)

    # Utiliza el formulario de autenticación personalizado en el admin
    login_form = CustomAuthenticationForm


# Registra el modelo de usuario personalizado y la clase UserAdmin en el admin
admin.site.register(User,UserAdmin)

# Inclusión de el modelo INVENTARIOS en la consola de administración de Django
@admin.register(SolicitudesExternas)
class SolicitudesExternasadmin(admin.ModelAdmin):
    list_display=('subject','name','email','mobile_number','department','message','lab','attach','registration_date','accept_politics',)
    list_per_page=10
    ordering=('id',)




