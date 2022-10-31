from django.contrib.gis.gdal.raster import source
from rest_framework import serializers
from Ferretic.models import *


class Empresa_serializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class Cliente_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class Proveedor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class ProductoPedido_serializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoPedido
        fields = '__all__'


class Sucursal_serializer(serializers.ModelSerializer):
    empresa = Empresa_serializer(readonly=True)
    empresa_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Empresa.objects.all(), source='empresa')
    class Meta:
        model = Sucursal
        fields = '__all__'


class Empleado_serializer(serializers.ModelSerializer):
    sucursal = Sucursal_serializer(readonly=True)
    sucursal_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Sucursal.objects.all(), source='sucursal')

    class Meta:
        model = Empleado
        fields = '__all__'

    def create(self, validated_data):
        user = Empleado(
            nombre=validated_data['nombre'],
            apellidos=validated_data['apellidos'],
            direccion=validated_data['direccion'],
            username=validated_data['username'],
            correo=validated_data['correo'],
            telefono=validated_data['telefono'],
            fecha_nacimiento=validated_data['fecha_nacimiento'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class Factura_serializer(serializers.ModelSerializer):
    cliente = Cliente_serializer(readonly=True)
    cliente_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Cliente.objects.all(), source='cliente')
    empleado = Empleado_serializer(readonly=True)
    empleado_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Empleado.objects.all(), source='empleado')

    class Meta:
        model = Factura
        fields = '__all__'


class Pedido_serializer(serializers.ModelSerializer):
    proveedor = Proveedor_serializer(readonly=True)
    proveedor_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Proveedor.objects.all(),
                                                      source='proveedor')
    producto_pedido = ProductoPedido_serializer(readonly=True)
    producto_pedido_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=ProductoPedido.objects.all(),
                                                            source='producto_pedido')

    class Meta:
        model = Pedido
        fields = '__all__'


class Inventario_serializer(serializers.ModelSerializer):
    sucursal = Sucursal_serializer(readonly=True)
    sucursal_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Sucursal.objects.all(), source='sucursal')
    pedido = Pedido_serializer(readonly=True)
    pedido_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Pedido.objects.all(), source='pedido')

    class Meta:
        model = Inventario
        fields = '__all__'


class Producto_serializer(serializers.ModelSerializer):
    inventario = Inventario_serializer(readonly=True)
    inventario_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Producto.objects.all(),
                                                       source='inventario')

    class Meta:
        model = Producto
        fields = '__all__'


class DetalleFactura_serializer(serializers.ModelSerializer):
    producto = Producto_serializer(readonly=True)
    producto_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Producto.objects.all(), source='producto')
    factura = Factura_serializer(readonly=True)
    factura_id = serializers.PrimaryKeyRelatedField(writeonly=True, queryset=Factura.objects.all(), source='factura')

    class Meta:
        model = DetalleFactura
        fields = '__all__'
