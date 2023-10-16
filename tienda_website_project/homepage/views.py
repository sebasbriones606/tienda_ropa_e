from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'homepage\home.html')

def login(request): 
    return render(request, 'homepage\login.html')

def logout(request):
    return render(request, 'homepage\logout.html')

def CarritoCompras(request): 
    return render(request, 'homepage\carritoCompras.html')    

def catalogo(request): 
    return render(request, 'homepage\catalogo.html')  

def Compra(request): 
    return render(request, 'homepage\compra.html')

def Dashboard(request): 
    return render(request, 'homepage\dashboard.html')
    
def GenerarPedido(request): 
    return render(request, 'homepage\generarPedido.html')   

def ProductoDetalle(request): 
    return render(request, 'homepage\productoDetalle.html')  

def Proveedores(request): 
    return render(request, 'homepage\Proveedores.html')

def PedidoRealizado(request): 
    return render(request, 'homepage\pedidoRealizado.html')

def RecuperacionContrasena(request): 
    return render(request, 'homepage\RecuperacionContrasena.html')    

def RegistrosUsuarios(request): 
    return render(request, 'homepage\RegistrosUsuarios.html')

@login_required
def Roles(request): 
    return render(request, 'homepage\Roles.html')

def contacto(request): 
    return render(request, 'homepage\contacto.html')

def ofertas(request): 
    return render(request, 'homepage\ofertas.html')

def VentasRealizadas(request): 
    return render(request, 'homepage\VentasRealizadas.html')   

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'homepage\productoDetalle.html', {'product': product})  
   
