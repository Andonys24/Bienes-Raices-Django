from django.shortcuts import render
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
