from rest_framework import status
from rest_framework.response import Response
from .models import Sede
from .serializers import SedeSerializer
from rest_framework import viewsets, mixins

class SedeView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    #mixins.DestroyModelMixin,
    #mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    
    