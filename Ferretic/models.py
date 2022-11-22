from django.contrib.auth.models import AbstractUser
from django.db import models


class Empresa(models.Model):
    razon_social = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    sitio_web = models.CharField(max_length=50)
    nit = models.CharField(max_length=20)
    representante_legal = models.CharField(max_length=50)

    def __str__(self):
        return self.razon_social


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    producto = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class ProductoPedido(models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    peso = models.FloatField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    ciudad = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    gerente = models.CharField(max_length=50)

    def __str__(self):
        return self.empresa.razon_social


class Empleado(AbstractUser):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, default=1)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(auto_now_add=False)
    token = models.CharField(max_length=100,null=True,blank=True,default='')

    def __str__(self):
        return self.first_name


class Factura(models.Model): ## pendiente id <----- TODO
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    fecha_venta = models.DateTimeField()

    def __str__(self):
        return 'Cliente ' + self.cliente.nombre + ' / Empleado' + self.empleado.nombre + ' Fecha: ' + self.fecha_venta


class Pedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    producto_pedido = models.ForeignKey(ProductoPedido, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    valor_unitario = models.FloatField()
    valor_total = models.FloatField()

    def __str__(self): ## agregar id pedido al return <--  TODO
        return 'Numero de pedido: ----Falta id pedido '+'/ Identificador proveedor '+self.proveedor.nombre


class Inventario(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    valor_neto = models.FloatField()
    existencias = models.IntegerField()

    def __str__(self):
        return 'Inventario de la sucursal de '+self.sucursal.empresa.razon_social+' de ' + self.sucursal.ciudad


class Producto(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    valor_comercial = models.FloatField()

    def __str__(self):
        return 'Nombre: '+self.nombre+' / Precio: '+ str(self.valor_comercial)


class DetalleFactura(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    valor_total = models.FloatField()

