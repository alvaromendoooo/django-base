from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import TipoMascota, Mascotas
from .serializers import TipoMascotaSerializer, MascotaSerializer


# ──────────────────────────────────────────────
#  TIPO MASCOTA
# ──────────────────────────────────────────────

class TipoMascotaListView(APIView):
    """
    GET  /mascotas/tipos/          → lista todos los tipos de mascota
    POST /mascotas/tipos/          → crea un nuevo tipo de mascota
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tipos = TipoMascota.objects.all()
        serializer = TipoMascotaSerializer(tipos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TipoMascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipoMascotaDetailView(APIView):
    """
    GET    /mascotas/tipos/<pk>/   → obtiene un tipo de mascota por su id
    PUT    /mascotas/tipos/<pk>/   → actualiza un tipo de mascota
    DELETE /mascotas/tipos/<pk>/   → elimina un tipo de mascota
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        tipo = get_object_or_404(TipoMascota, pk=pk)
        serializer = TipoMascotaSerializer(tipo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        tipo = get_object_or_404(TipoMascota, pk=pk)
        serializer = TipoMascotaSerializer(tipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tipo = get_object_or_404(TipoMascota, pk=pk)
        tipo.delete()
        return Response(
            {"detail": "Tipo de mascota eliminado correctamente."},
            status=status.HTTP_204_NO_CONTENT
        )


# ──────────────────────────────────────────────
#  MASCOTAS
# ──────────────────────────────────────────────

class MascotaListView(APIView):
    """
    GET  /mascotas/                → lista todas las mascotas del usuario autenticado
    POST /mascotas/                → registra una nueva mascota para el usuario autenticado
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mascotas = Mascotas.objects.filter(owner=request.user)
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MascotaDetailView(APIView):
    """
    GET    /mascotas/<pk>/         → obtiene una mascota por su id
    PUT    /mascotas/<pk>/         → actualiza una mascota (solo su dueño)
    DELETE /mascotas/<pk>/         → elimina una mascota (solo su dueño)
    """
    permission_classes = [IsAuthenticated]

    def _get_mascota_owner(self, pk, user):
        """Devuelve la mascota si pertenece al usuario, 404 si no existe, 403 si no es el dueño."""
        mascota = get_object_or_404(Mascotas, pk=pk)
        if mascota.owner != user:
            return None, Response(
                {"detail": "No tienes permiso para acceder a esta mascota."},
                status=status.HTTP_403_FORBIDDEN
            )
        return mascota, None

    def get(self, request, pk):
        mascota = get_object_or_404(Mascotas, pk=pk)
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        mascota, error = self._get_mascota_owner(pk, request.user)
        if error:
            return error
        serializer = MascotaSerializer(mascota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mascota, error = self._get_mascota_owner(pk, request.user)
        if error:
            return error
        mascota.delete()
        return Response(
            {"detail": "Mascota eliminada correctamente."},
            status=status.HTTP_204_NO_CONTENT
        )
