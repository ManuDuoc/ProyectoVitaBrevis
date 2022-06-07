from django.shortcuts import render, redirect
from .models import Categoria, Producto
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def inicio(request):
    Productos = Producto.objects.all()
    Categorias= Categoria.objects.all()
    contexto = {
        "Productos" : Productos,
        "categoria" : Categorias
    }
    return render(request,'core/Principal.html', contexto)

def PS5(request):
    return render(request,'core/PS5.html')

def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('login')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'core/registro.html', context)

def login(request):
    return render(request,'core/inicio.html')

def usuario(request):
    categorias= Categoria.objects.all()
    return render(request,'core/usuarios.html',{"cate":categorias})

def logout(request):
    return render(request,'core/logout.html')

def Usuarios(request):
    categorias= User.objects.all() #me trae todos los registros de esa tabla (select * from)
    return render(request,'core/listaUsuarios.html',{"usuario":categorias})

def eliminarUsuario(request, id):
    produc = User.objects.get(id=id)
    produc.delete()
    messages.success(request,'Usuario Eliminado')
    return redirect('listaUsuarios')

def Categorias(request,nombreCategoria):
    categorias= Categoria.objects.get(nombreCategoria=nombreCategoria)
    Productos = Producto.objects.all()
    cate = Categoria.objects.all()
    contexto = {
        "Productos" : Productos,
        "categoria" : categorias,
        "cate" : cate
    }
    return render(request,'core/Categoria.html',contexto)

def administrador(request): 
    return render(request,'core/administrador.html') 

def inicios(request):
    Productos = Producto.objects.all()
    Categorias= Categoria.objects.all()
    contexto = {
        "Productos" : Productos,
        "categoria" : Categorias
    }
    return render(request,'core/inicio.html',contexto)

def anadirjuego(request):
    categorias = Categoria.objects.all() #me trae todos los registros de esa tabla (select * from)
    contexto = {"categoria_m":categorias}
    return render(request,'core/anadirjuego.html',contexto)

def Juego(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    cate = Categoria.objects.all()
    contexto = {
        "produc" : producto,
        "cate" : cate
    }
    return render(request,'core/Juegos.html',contexto)

def listajuegos(request):
    Productos = Producto.objects.all()
    return render(request,'core/listajuegos.html',{"Productos": Productos})

def listar_Categoria(request):
    categorias = Categoria.objects.all() #me trae todos los registros de esa tabla (select * from)
    return render(request,'core/anadirjuego.html',{"categoria_m":categorias})


def registrarjuego(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['txtPrecio']
    categoria_m = request.POST['categoria']
    stock = request.POST['txtStock']
    f = request.FILES['file']
    video = request.POST['txtVideo']
    descripcion = request.POST['txtDescripcion']
    masInfo1 = request.POST['txtMasInfo1']
    masInfo2 = request.POST['txtMasInfo2']
    masInfo3 = request.POST['txtMasInfo3']
    masInfo4 = request.POST['txtMasInfo4']
    masInfo5 = request.POST['txtMasInfo5']
    categoria_c = Categoria.objects.get(codigo = categoria_m)

    Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, categoria=categoria_c, stock=stock, foto=f, video=video, descripcion=descripcion, masInfo1=masInfo1, masInfo2=masInfo2, masInfo3=masInfo3, masInfo4=masInfo4, masInfo5=masInfo5)
    messages.success(request,'Juego Registrado')
    return redirect('listajuegos')

def eliminarJuego(request, codigo):
    produc = Producto.objects.get(codigo=codigo)
    produc.delete()
    return redirect('listajuegos')
    

def edicionJuegos(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    categorias = Categoria.objects.all()
    contexto = {
        "produc" : producto,
        "categoria" : categorias
    }
    return render(request,"core/edicionJuegos.html",contexto)

def editarjuego(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['txtPrecio']
    stock = request.POST['txtStock']
    categoria_m = request.POST['categoria']
    video = request.POST['txtVideo']
    descripcion = request.POST['txtDescripcion']
    masInfo1 = request.POST['txtMasInfo1']
    masInfo2 = request.POST['txtMasInfo2']
    masInfo3 = request.POST['txtMasInfo3']
    masInfo4 = request.POST['txtMasInfo4']
    masInfo5 = request.POST['txtMasInfo5']
    produc = Producto.objects.get(codigo=codigo)
    if(request.FILES.get("file")):
        f = request.FILES["file"]
        produc.foto = f


    produc.codigo = codigo
    produc.nombre = nombre
    produc.precio = precio
    produc.stock = stock
    produc.video = video
    produc.descripcion = descripcion
    produc.masInfo1 = masInfo1
    produc.masInfo2 = masInfo2
    produc.masInfo3 = masInfo3
    produc.masInfo4 = masInfo4
    produc.masInfo5 = masInfo5
    categoria_c = Categoria.objects.get(codigo = categoria_m)
    produc.categoria = categoria_c
    produc.save()
    return redirect('listajuegos')

