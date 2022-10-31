from django.shortcuts import render
from rest_framework import viewsets
from ferretic.serializer import *
from Ferretic.models import *


class Empresa_view(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = Empresa_serializer

class Cliente_view(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = Cliente_serializer

class Proveedor_view(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = Proveedor_serializer

class ProductoPedido_view(viewsets.ModelViewSet):
    queryset = ProductoPedido.objects.all()
    serializer_class = ProductoPedido_serializer

class Sucursal_view(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = Sucursal_serializer

class Empleado_view(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = Empleado_serializer

class Factura_view(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = Facttura_serializer

class Pedido_view(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = Pedido_serializer

class Inventario_view(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = Inventario_serializer

class Producto_view(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Producto_serializer

class DetalleFactura_view(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFactura_serializer


