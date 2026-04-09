from django.db import models
from user.models import User
from mascotas.models import TipoMascota

# Create your models here.
class Encuentro(models.Model):
    fecha = models.DateTimeField("Fecha", null = False, auto_now_add = False, blank = False)
    localizacion = models.CharField("Localizacion", null = False, blank = False, max_length = 300)
    limite_usuarios = models.IntegerField("Limite de usuarios", null = True, blank = True, default = 1)
    duracion_minutos = models.IntegerField("Duracion", null = True, blank = True)
    descripcion = models.CharField("Descripcion", null = True, blank = True, max_length = 200)
    titulo = models.CharField("Titulo", null = False, blank = False, max_length = 100)

    tipo_mascota = models.ForeignKey(
        TipoMascota,
        on_delete = models.SET_NULL,
        related_name = "mascota_permitida",
        null = True,
    )

    creador = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "creado_por"
    )

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"
