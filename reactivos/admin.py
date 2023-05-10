from django.contrib import admin
from .models import *

@admin.register(Unidades)
class Unidadesadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)
  
@admin.register(Marcas)
class Marcasadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)


@admin.register(Reactivos)
class Reactivosadmin(admin.ModelAdmin):
    list_display=('id','code','cas','name','is_liquid','unit','is_active','wlocation')
    list_filter=('code','name',)
    search_fields=('code','name',)
    list_editable=('is_active',)
    list_per_page=10
    ordering=('id',)


@admin.register(Destinos)
class Destinoadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)




@admin.register(Ubicaciones)
class Ubicacionadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)



@admin.register(Responsables)
class Responsableadmin(admin.ModelAdmin):
    list_display=('id','name','mail','phone','is_active',)
    ordering=('id',)


@admin.register(Salidas)
class Salidaadmin(admin.ModelAdmin):
    list_display=('id','date','name','trademark','reference','weight','is_liquid','destination','manager','observations','location')
    list_filter=('date','name',)
    search_fields=('date','name',)
    list_per_page=10
    ordering=('id',)

@admin.register(Entradas)
class Salidaadmin(admin.ModelAdmin):
    list_display=('id','date','name','trademark','reference','weight','is_liquid','order','manager','observations','location')
    list_filter=('date','name',)
    search_fields=('date','name',)
    list_per_page=10
    ordering=('id',)

