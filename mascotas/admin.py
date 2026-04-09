from django.contrib import admin
from .models import TipoMascota, Mascotas


@admin.register(TipoMascota)
class TipoMascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'codigo')
    search_fields = ('nombre', 'codigo')
    ordering = ('nombre',)


@admin.register(Mascotas)
class MascotasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_mascota', 'owner')
    search_fields = ('nombre', 'owner__username')
    list_filter = ('tipo_mascota',)
    ordering = ('nombre',)
from django.contrib import admin

# Register your models here.
