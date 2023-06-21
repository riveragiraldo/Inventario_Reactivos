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





@admin.register(Destinos)
class Destinoadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)

@admin.register(Estados)
class Estadoadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)



@admin.register(Ubicaciones)
class Ubicacionadmin(admin.ModelAdmin):
    list_display=('id','name','facultad')
    ordering=('id',)

@admin.register(Facultades)
class Facultadadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)

@admin.register(RespelC)
class Respeladmin(admin.ModelAdmin):
    list_display=('id','name','description')
    ordering=('id',)


@admin.register(SGA)
class SGIadmin(admin.ModelAdmin):
    list_display=('id','name','description')
    ordering=('id',)

@admin.register(Laboratorios)
class Laboratorioadmin(admin.ModelAdmin):
    list_display=('id','name','fecha_registro')
    ordering=('id',)



@admin.register(Responsables)
class Responsableadmin(admin.ModelAdmin):
    list_display=('id','name','mail','phone','is_active',)
    ordering=('id',)

@admin.register(Almacenamiento)
class Alamacenamientoadmin(admin.ModelAdmin):
    list_display=('id','lab','name','description',)
    ordering=('id',)


@admin.register(Reactivos)
class Reactivosadmin(admin.ModelAdmin):
    list_display=('id','code','cas','name','state','unit','respel','sga','fecha_registro')
    list_filter=('code','name',)
    search_fields=('code','name',)
    list_per_page=10
    ordering=('id',)




@admin.register(Entradas)
class Entradaadmin(admin.ModelAdmin):
    list_display=('id','date','name','trademark','reference','weight','order','manager','observations','location','price','edate','nproject','destination','lab',)
    list_filter=('date','name','lab',)
    search_fields=('date','name','lab',)
    list_per_page=10
    ordering=('id',)

@admin.register(Salidas)
class Salidaadmin(admin.ModelAdmin):
    list_display=('id','date','name','trademark','reference','weight','destination','manager','observations','location','lab')
    list_filter=('date','name','lab')
    search_fields=('date','name','lab')
    list_per_page=10
    ordering=('id',)

@admin.register(Inventarios)
class Inventarioadmin(admin.ModelAdmin):
    list_display=('id','name','trademark','weight','unit','reference','lab','fecha_registro','wlocation',)
    list_filter=('trademark','name','reference','lab',)
    search_fields=('trademark','name','reference','lab',)
    list_per_page=10
    ordering=('id',)



