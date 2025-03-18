from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns =  [
    path('',views.portada),
    path('editar/<codigo>', views.edicionProducto),
    path('editarproducto/',views.editarproducto),
    path('eliminar/<codigo>',views.eliminarProducto),
    path('comprar/<codigo>',views.comprarProducto),
    path('scan/', views.scan_barcode, name='scan_barcode'),
    path('barcode/', csrf_exempt(views.barcode_scanner), name='barcode_scanner')
]