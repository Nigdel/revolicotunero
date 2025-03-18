from django.shortcuts import render,redirect
from .models import Producto
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def portada(request):
    prod = Producto.objects.filter(cantidad__gte = 1)
    # prod = Producto.objects.all()
    if request.method == "POST":
       codigo = request.POST['codigo']
       nombre = request.POST['nombre']
       precio = request.POST['precio']
       cantidad = request.POST['cantidad']
       if cantidad and codigo and precio and nombre :
            producto_nuevo = Producto.objects.create(
                codigo = codigo, nombre = nombre, precio = precio, cantidad= cantidad
            )
       else:
            messages.success(request,"Datos incompletos para adicionar un producto")
    return render(request,'portada.html',{'productos':prod})

def edicionProducto(request,codigo):
    prod = Producto.objects.get(codigo=codigo)
    if prod:
        return render(request,'editarProducto.html', {'producto': prod})
    else:
        messages.success(request,"No se encontro el producto con codigo %d" , codigo)
        return redirect('/')
def editarproducto(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    cantidad = request.POST['cantidad']
    prod = Producto.objects.get(codigo=codigo)
    prod.nombre = nombre
    prod.precio = precio
    prod.cantidad = cantidad
    prod.save()
    return redirect('/')

def eliminarProducto(request,codigo):
    prod = Producto.objects.get(codigo=codigo)
    prod.delete()

    return redirect('/')

def comprarProducto(request,codigo):
    prod = Producto.objects.get(codigo=codigo)
    if prod:
        if prod.cantidad - 1 >= 0:
            prod.cantidad= prod.cantidad -1
            prod.save()
            # if prod.cantidad==0:
            #     prod.delete()

    else:
        messages.success(request,"No se encontro el producto con codigo %d" , codigo)
    return redirect('/')

@api_view(['POST'])
def scan_barcode(request):
    code = request.data.get('code')
    if code:
        return Response({"message": f"Código recibido: {code}"})
    return Response({"error": f"No se envió ningún código{request.data}"}, status=400)

def barcode_scanner(request):
    return render(request, 'barcode_scanner.html')
