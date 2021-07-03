from django.contrib import admin
from productos.models import Producto, Marca, Categoria
from cart.models import Order, OrderItem

# Register your models here.
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Order)
admin.site.register(OrderItem)