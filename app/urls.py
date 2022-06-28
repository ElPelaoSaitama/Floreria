from django.urls import path
from .views import home, contacto, galeria, registro,\
    agregar_producto, listar_productos


urlpatterns = [
    path('', home,name="home"),
    path('contacto/', contacto,name="contacto"),
    path('galeria/', galeria,name="galeria"),
    path('registro/', registro, name="registro"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
     path('listar-productos/', listar_productos, name="listar_productos"),
]
