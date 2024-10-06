from django.shortcuts import render
from django.contrib import messages
from propiedades.models import Propiedad


# Create your views here.
def index(request):
    propiedades = Propiedad.objects.all()
    return render(
        request,
        "administrador/index.html",
        {"titulo": "Administración de Bienes Raíces", "propiedades": propiedades},
    )
