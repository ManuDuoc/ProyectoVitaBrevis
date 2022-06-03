from msilib.schema import File
from pickle import FALSE
from django.shortcuts import render, redirect
from .models import Categoria, Juego, Producto
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request,'core/Principal.html')

def PS5(request):
    return render(request,'core/PS5.html')

def registro(request):
    return render(request,'core/registro.html')

def login(request):
    return render(request,'core/login.html')

def accion(request):
    return render(request,'core/accion.html')

def deporte(request):
    return render(request,'core/deporte.html')

def simulacion(request):
    return render(request,'core/simulacion.html')

def terror(request):
    return render(request,'core/terror.html')

def administrador(request):
    return render(request,'core/administrador.html')    

def anadirjuego(request):
    categorias = Categoria.objects.all() #me trae todos los registros de esa tabla (select * from)
    contexto = {"categoria_m":categorias}
    return render(request,'core/anadirjuego.html',contexto)
    
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
    f = request.FILES['file']
    video = request.POST['txtVideo']
    descripcion = request.POST['txtDescripcion']
    masInfo1 = request.POST['txtMasInfo1']
    masInfo2 = request.POST['txtMasInfo2']
    masInfo3 = request.POST['txtMasInfo3']
    masInfo4 = request.POST['txtMasInfo4']
    masInfo5 = request.POST['txtMasInfo5']
    categoria_c = Categoria.objects.get(codigo = categoria_m)

    Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, categoria=categoria_c, foto=f, video=video, descripcion=descripcion, masInfo1=masInfo1, masInfo2=masInfo2, masInfo3=masInfo3, masInfo4=masInfo4, masInfo5=masInfo5)
    messages.success(request,'Juego Registrado')
    return redirect('/')

def juego(request):
    contexto = {"titulo":"Fifa 22","ImagenJ":"/static/core/img/Deportes/fifa_22.jpeg",
                "NombreJ":"Fifa 22 Key",
                "descripcion":"Desarrollado por Football ™, EA SPORTS ™ FIFA 22 acerca el juego aún más a la realidad con avances fundamentales en el juego y una nueva temporada de innovación en todos los modos.Las nuevas características de juego en FIFA 22 te brindan más consistencia entre las publicaciones con una reescritura del portero que brinda más compostura a la posición más importante en el campo, junto con una nueva física de la pelota, un sprint explosivo que se adapta mejor a la aceleración de los jugadores más rápidos del juego y nuevas tácticas de ataque que te permiten tomar el control de cómo juega tu equipo.",
                "PrecioJ":"$19.990","VideoJ":"https://www.youtube.com/embed/SYsi5QuOJNE",
                "Info1":"COMO SE JUEGA: El juego reinventado crea avances fundamentales que sentirás en todos los modos de FIFA 22. Una reescritura del portero aporta más compostura y consistencia a la posición más importante en la cancha, la nueva física del balón reinventa cada pase, tiro y gol, y un sprint explosivo permite sientes la aceleración de los jugadores más rápidos del juego.",
                "Info2":"FÍSICA DEL BALÓN REAL: Los datos del mundo real importados a FIFA 22 llevan la física del balón del juego a un nuevo nivel de realismo. Los parámetros ajustados que incluyen velocidad, viraje, arrastre de aire, resistencia del aire, fricción del suelo y fricción de rodadura significan que cada toque, trampa, disparo, volea, pase y regate se verá, se moverá y volará como si fuera real.",
                "Info3":"MODO DE CARRERA: Vive tus sueños futbolísticos en el modo Carrera de FIFA 22 mientras creas un club y los llevas de candidatos al descenso a gigantes globales, y disfruta de una experiencia de carrera de jugador renovada que te brinda más formas de progresar, lograr y sumergirte en el viaje de tu profesional. el juego.",
                "Info4":"EQUIPO ULTIMATE DE FIFA: Crea el equipo de tus sueños y compite en el modo más popular de FIFA, con miles de jugadores para agregar a tu club e innumerables formas de personalizar tu club dentro y fuera de la cancha. Ya sea que quieras jugar por tu cuenta en Squad Battles, juntos en FUT Co-Op, en línea en Division Rivals o contra los mejores en FUT Champions, FIFA Ultimate Team ™ (FUT) te conecta con el mundo del fútbol durante toda la temporada. con una variedad de contenido influenciado por actuaciones y competiciones del mundo real, como la UEFA Champions League, la UEFA Europa League y la CONMEBOL Libertadores.",
                "Info5":"AUTENTICIDAD INIGUALABLE: Experimenta una autenticidad incomparable en FIFA 22 con la experiencia más realista del Juego del Mundo con las estrellas y equipos más importantes del fútbol. Con más de 17,000 jugadores en más de 700 equipos en más de 90 estadios y más de 30 ligas, FIFA 22 es el único lugar donde puedes jugar la icónica UEFA Champions League, UEFA Europa League, la nueva UEFA Europa Conference League, CONMEBOL Libertadores, CONMEBOL Sudamericana, Premier League, Bundesliga y LaLiga Santander."}
    return render(request,'core/juego.html',contexto)