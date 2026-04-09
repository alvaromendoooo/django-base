from django.db import models
from user.models import User

# Create your models here.
class TipoMascota(models.Model):
    nombre = models.CharField("Raza", max_length = 50, null = False, blank = False)
    codigo = models.CharField("Codigo", max_length = 8, null = False, blank = False, unique = True)

    def __str__(self):
        return f"{self.nombre} - {self.codigo}"

class Mascotas(models.Model):
    nombre = models.CharField("Nombre", max_length = 50, blank = False, null = False)
    descripcion = models.CharField("Descripcion", max_length = 300, blank = False, null = True)
    foto = models.FileField("Foto", null = True, blank = True)

    tipo_mascota = models.ForeignKey(
        TipoMascota,
        on_delete = models.SET_NULL,
        null = True, 
        related_name = "mascotas"
    )

    owner = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "mascotas",
        null = False
    )

    def __str__(self):
        return f"{self.nombre}"