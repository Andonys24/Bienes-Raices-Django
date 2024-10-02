from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, "index.html", {'titulo': 'Inicio'})

def nosotros(request):
    return render(request, "nosotros.html", {'titulo': 'Nosotros'})

def anuncios(request):
    return render(request, "anuncios.html", {'titulo': 'Anuncios'})

def anuncio(request):
    return render(request, "anuncio.html", {'titulo': 'Anuncio'})

def blog(request):
    return render(request, "blog.html", {'titulo': 'Nuestro Blog'})

def entrada(request):
    return render(request, 'entrada.html', {'titulo': 'Entrada'})

def contacto(request):
    return render(request, "contacto.html", {'titulo': 'Contacto'})