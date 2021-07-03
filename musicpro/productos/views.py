from django.shortcuts import render
from .serializers import ProductoSerializer, TipoSerializer
from .models import Producto, Marca
from rest_framework import viewsets

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = TipoSerializer