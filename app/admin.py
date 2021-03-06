from django.contrib import admin
from .models import Marca,Producto, Contacto
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio","disponible","marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca","disponible"]
    list_per_page = 25


admin.site.register(Marca)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Contacto)


