from django.shortcuts import render
from rest_framework import viewsets, mixins

from .models import Proveedor
from .serializers import *

class ProveedorView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    #mixins.DestroyModelMixin,
    #mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    def get_queryset(self):
        
        nombre = self.request.query_params.get('nombre')

        if nombre:
            self.queryset = self.queryset.filter(name__icontains=nombre)

        return self.queryset
