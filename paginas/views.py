from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from propiedades.models import Propiedad


# Create your views here.
def inicio(request):
    propiedades = Propiedad.objects.order_by("-id")[:3]
    return render(
        request, "index.html", {"titulo": "Inicio", "propiedades": propiedades}
    )


def nosotros(request):
    return render(request, "nosotros.html", {"titulo": "Nosotros"})


def anuncios(request):
    propiedades = Propiedad.objects.all()
    return render(
        request, "anuncios.html", {"titulo": "Anuncios", "propiedades": propiedades}
    )


def anuncio(request, id):
    propiedad = Propiedad.objects.get(pk=id)
    return render(
        request, "anuncio.html", {"titulo": propiedad.titulo, "propiedad": propiedad}
    )


def blog(request):
    return render(request, "blog.html", {"titulo": "Nuestro Blog"})


def entrada(request):
    return render(request, "entrada.html", {"titulo": "Entrada"})


def contacto(request):
    return render(request, "contacto.html", {"titulo": "Contacto"})


def pagina_404(request, exception):
    return render(request, "404.html", {"titulo": "Página no encontrada"}, status=404)


def login_page(request):
    if request.user.is_authenticated:
        return redirect("administracion")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Usuario no existente")
        else:
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, "Sesión iniciada correctamente", extra_tags="exito")
                return redirect("administracion")
            else:
                messages.error(request, "Contraseña incorrecta")

    return render(request, "login.html", {"titulo": "Iniciar Sesión"})

def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente", extra_tags="exito")
    return redirect("inicio")