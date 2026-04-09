from rest_framework import serializers
from .models import TipoMascota, Mascotas


class TipoMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMascota
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    tipo_mascota_detalle = TipoMascotaSerializer(source='tipo_mascota', read_only=True)

    class Meta:
        model = Mascotas
        fields = ['id', 'nombre', 'descripcion', 'foto', 'tipo_mascota', 'tipo_mascota_detalle', 'owner']
        extra_kwargs = {
            'tipo_mascota': {'write_only': True},
            'owner': {'read_only': True},
        }
