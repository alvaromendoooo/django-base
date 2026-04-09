from rest_framework import serializers
from .models import Encuentro
from mascotas.serializers import TipoMascotaSerializer


class EncuentroSerializer(serializers.ModelSerializer):
    tipo_mascota_detalle = TipoMascotaSerializer(source='tipo_mascota', read_only=True)

    class Meta:
        model = Encuentro
        fields = [
            'id',
            'titulo',
            'descripcion',
            'fecha',
            'localizacion',
            'limite_usuarios',
            'duracion_minutos',
            'tipo_mascota',
            'tipo_mascota_detalle',
            'creador',
        ]
        extra_kwargs = {
            'tipo_mascota': {'write_only': True},
            'creador': {'read_only': True},
        }
