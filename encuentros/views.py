from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Encuentro
from .serializers import EncuentroSerializer


class EncuentroListView(APIView):
    """
    GET  /encuentros/                              → lista todos los encuentros
    GET  /encuentros/?tipo_mascota=<pk>            → filtra encuentros por tipo de mascota
    GET  /encuentros/?fecha=<YYYY-MM-DD>           → filtra encuentros por fecha
    POST /encuentros/                              → crea un nuevo encuentro
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        encuentros = Encuentro.objects.all()

        # Filtro por tipo de mascota (query param: ?tipo_mascota=<pk>)
        tipo_mascota_id = request.query_params.get('tipo_mascota')
        if tipo_mascota_id:
            encuentros = encuentros.filter(tipo_mascota__id=tipo_mascota_id)

        # Filtro adicional por fecha (query param: ?fecha=YYYY-MM-DD)
        fecha = request.query_params.get('fecha')
        if fecha:
            encuentros = encuentros.filter(fecha__date=fecha)

        serializer = EncuentroSerializer(encuentros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EncuentroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creador=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EncuentroDetailView(APIView):
    """
    GET    /encuentros/<pk>/       → obtiene un encuentro por su id
    PUT    /encuentros/<pk>/       → actualiza un encuentro (solo su creador)
    DELETE /encuentros/<pk>/       → elimina un encuentro (solo su creador)
    """
    permission_classes = [IsAuthenticated]

    def _get_encuentro_creador(self, pk, user):
        """Devuelve el encuentro si pertenece al usuario, 403 si no es el creador."""
        encuentro = get_object_or_404(Encuentro, pk=pk)
        if encuentro.creador != user:
            return None, Response(
                {"detail": "Solo el creador puede modificar o eliminar este encuentro."},
                status=status.HTTP_403_FORBIDDEN
            )
        return encuentro, None

    def get(self, request, pk):
        encuentro = get_object_or_404(Encuentro, pk=pk)
        serializer = EncuentroSerializer(encuentro)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        encuentro, error = self._get_encuentro_creador(pk, request.user)
        if error:
            return error
        serializer = EncuentroSerializer(encuentro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        encuentro, error = self._get_encuentro_creador(pk, request.user)
        if error:
            return error
        encuentro.delete()
        return Response(
            {"detail": "Encuentro eliminado correctamente."},
            status=status.HTTP_204_NO_CONTENT
        )
