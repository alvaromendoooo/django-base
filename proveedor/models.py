from django.db import models

# Create your models here.
class Proveedor(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.CharField('Descripcion', max_length = 300)
    codigo = models.CharField('Codigo', max_length = 8)

    def __str__(self):
        return f"{self.name} - {self.codigo}"