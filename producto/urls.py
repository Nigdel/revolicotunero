from django.urls import path
from . import views

urlpatterns =  [
    path('',views.portada),
    path('editar/<codigo>', views.edicionProducto),
    path('editarproducto/',views.editarproducto),
    path('eliminar/<codigo>',views.eliminarProducto),
    path('comprar/<codigo>',views.comprarProducto)
]