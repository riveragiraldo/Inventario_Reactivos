# En este archivo se configuran las opciones de administración de Django

from django.contrib import admin
from .models import *

# Inclusión de el modelo UNIDADES en la consola de administración de Django
@admin.register(Unidades)
class Unidadesadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)

# Inclusión de el modelo MARCAS en la consola de administración de Django  
@admin.register(Marcas)
class Marcasadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)

# Inclusión de el modelo DESTINOS en la consola de administración de Django    
@admin.register(Destinos)
class Destinoadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)

# Inclusión de el modelo ESTADOS en la consola de administración de Django
@admin.register(Estados)
class Estadoadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)

# Inclusión de el modelo UBICACIONES en la consola de administración de Django
@admin.register(Ubicaciones)
class Ubicacionadmin(admin.ModelAdmin):
    list_display=('id','name','facultad')
    ordering=('id',)

# Inclusión de el modelo FACULTADES en la consola de administración de Django
@admin.register(Facultades)
class Facultadadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)

# Inclusión de el modelo CLASIFICACIÓN RESPEL en la consola de administración de Django
@admin.register(RespelC)
class Respeladmin(admin.ModelAdmin):
    list_display=('id','name','description')
    ordering=('id',)

# Inclusión de el modelo CLASIFICACIÓN SGA en la consola de administración de Django
@admin.register(SGA)
class SGIadmin(admin.ModelAdmin):
    list_display=('id','name','description')
    ordering=('id',)

# Inclusión de el modelo LABORATORIOS en la consola de administración de Django
@admin.register(Laboratorios)
class Laboratorioadmin(admin.ModelAdmin):
    list_display=('id','name','fecha_registro')
    ordering=('id',)

# Inclusión de el modelo RESPONSABLES en la consola de administración de Django
@admin.register(Responsables)
class Responsableadmin(admin.ModelAdmin):
    list_display=('id','name','mail','phone','is_active',)
    ordering=('id',)

# Inclusión de el modelo ALMACENAMIENTO en la consola de administración de Django
@admin.register(Almacenamiento)
class Alamacenamientoadmin(admin.ModelAdmin):
    list_display=('id','lab','name','description',)
    ordering=('id',)

# Inclusión de el modelo REACTIVOS en la consola de administración de Django
@admin.register(Reactivos)
class Reactivosadmin(admin.ModelAdmin):
    list_display=('id','code','cas','name','state','unit','respel','sga','fecha_registro')
    list_filter=('code','name',)
    search_fields=('code','name',)
    list_per_page=10
    ordering=('id',)

# Inclusión de el modelo ENTRADAS en la consola de administración de Django
@admin.register(Entradas)
class Entradaadmin(admin.ModelAdmin):
    list_display=('id','date','name','trademark','reference','weight','order','manager','observations','location','price','nproject','destination','lab',)
    list_filter=('date','name','lab',)
    search_fields=('date','name','lab',)
    list_per_page=10
    ordering=('id',)

# Inclusión de el modelo SALIDAS en la consola de administración de Django
@admin.register(Salidas)
class Salidaadmin(admin.ModelAdmin):
    list_display=('id','date','name','trademark','reference','weight','destination','manager','observations','location','lab')
    list_filter=('date','name','lab')
    search_fields=('date','name','lab')
    list_per_page=10
    ordering=('id',)

# Inclusión de el modelo INVENTARIOS en la consola de administración de Django
@admin.register(Inventarios)
class Inventarioadmin(admin.ModelAdmin):
    list_display=('id','name','trademark','weight','unit','reference','lab','fecha_registro','wlocation','minstock','edate','is_active')
    list_filter=('trademark','name','reference','lab',)
    search_fields=('trademark','name','reference','lab',)
    list_per_page=10
    ordering=('id',)



