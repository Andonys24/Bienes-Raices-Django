from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from propiedades.models import Propiedad


# Create your views here.
@login_required(login_url="login")
def index(request):
    propiedades = Propiedad.objects.all()
    return render(
        request,
        "administrador/index.html",
        {"titulo": "Administración de Bienes Raíces", "propiedades": propiedades},
    )
