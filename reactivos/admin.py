from django.contrib import admin
from .models import Reactivos, Unidades

@admin.register(Unidades)
class Unidadesadmin(admin.ModelAdmin):
    list_display=('id','name',)
    ordering=('id',)
  

@admin.register(Reactivos)
class Reactivosadmin(admin.ModelAdmin):
    list_display=('id','code','name','unit','is_active',)
    list_filter=('code','name',)
    search_fields=('code','name',)
    list_editable=('is_active',)
    list_per_page=10
    ordering=('id',)
