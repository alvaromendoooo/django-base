from rest_framework import status
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets

# Create your views here.
class ProductoView(
    viewsets.ModelViewSet,
):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


    def list(self, request):
        """
        If the action is list, then try to get the query parameter "select" and return the filtered
        queryset. If the query parameter "select" doesn't exist, then return all objects. If the action
        is not list, then return all objects

        :return: List of all products.
        """

        result = Producto.objects.all()
        return Response(self.serializer_class(result, many=True).data, status=200)

    def create(self, request, *args, **kwargs):
        """
        It creates a new object, then returns a response with a success message

        :param request: The request object

        :return: The response is a dictionary with a key of "success" and a value of "ok."
        """
        try:
            super().create(request, *args, **kwargs)
            return Response({"success": "ok"}, status=201)
        except ValueError:
            return Response({"error": "Invalid date"}, status=400)
