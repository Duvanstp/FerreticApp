from django.urls import path, include
from rest_framework import routers
from Ferretic.views import *


router = routers.DefaultRouter()
router.register('empresa',Empresa_view,basename='empresa')
router.register('cliente',Cliente_view,basename='cliente')
router.register('proveedor',Proveedor_view,basename='proveedor')
router.register('productopedido',ProductoPedido_view,basename='productopedido')
router.register('sucursal',Sucursal_view,basename='sucursal')
router.register('empleado',Empleado_view,basename='empleado')
router.register('factura',Factura_view,basename='factura')
router.register('pedido',Pedido_view,basename='pedido')
router.register('inventario',Inventario_view,basename='inventario')
router.register('producto',Producto_view,basename='producto')
router.register('detallefactura',DetalleFactura_view,basename='detallefactura')


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token', TokenProvider.as_view(), name='token'),
]
