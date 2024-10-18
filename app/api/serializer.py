
# Django
from rest_framework import serializers

# Propios
from app.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['pk', 'descripcion']

    read_only_fields = ['pk']
