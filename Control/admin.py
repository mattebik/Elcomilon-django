
from django.contrib import admin
from Control.models import Proveedor, Producto, Bitacora, Bodega, Boletas, Cliente, Delivery
# Register your models here.

class ProductoAdmin(admin.ModelAdmin): 
    list_filter=("tipo",)


admin.site.register(Bitacora)
admin.site.register(Bodega)
admin.site.register(Boletas)
admin.site.register(Cliente)
admin.site.register(Delivery)
admin.site.register(Proveedor)
admin.site.register(Producto, ProductoAdmin)
