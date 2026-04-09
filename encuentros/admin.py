from django.contrib import admin
from .models import Encuentro


@admin.register(Encuentro)
class EncuentroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'localizacion', 'tipo_mascota', 'creador', 'limite_usuarios')
    search_fields = ('titulo', 'localizacion', 'creador__username')
    list_filter = ('tipo_mascota', 'fecha')
    ordering = ('-fecha',)
