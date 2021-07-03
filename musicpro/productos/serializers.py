from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Producto, Marca

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'