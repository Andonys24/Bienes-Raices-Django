from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Vendedor
from .forms import VendedorForm
from propiedades.models import Propiedad


# Create your views here.
@login_required(login_url="login")
def index(request):
    vendedores = Vendedor.objects.all()
    return render(
        request,
        "vendedores/index.html",
        {"titulo": "Vendedores", "vendedores": vendedores},
    )


@login_required(login_url="login")
def agregar(request):
    if request.method == "POST":
        formulario = VendedorForm(request.POST)
        if formulario.is_valid():
            vendedor = formulario.save(commit=False)
            vendedor.save()
            messages.success(
                request, "Vendedor agregado correctamente", extra_tags="exito"
            )
            return redirect("vendedores")
        else:
            alertas = None
            for field, errores in formulario.errors.items():
                alertas = errores[0]
                break
    else:
        formulario = VendedorForm()
        alertas = None
    return render(
        request,
        "vendedores/crear.html",
        {"titulo": "Agregar vendedor", "formulario": formulario, "alertas": alertas},
    )


@login_required(login_url="login")
def editar(request, id):
    try:
        vendedor = Vendedor.objects.get(pk=id)
    except Vendedor.DoesNotExist:
        messages.error(request, "Vendedor no encontrado", extra_tags="error")
        return redirect("vendedores")
    if request.method == "POST":
        formulario = VendedorForm(request.POST, instance=vendedor)
        if formulario.is_valid():
            vendedor = formulario.save()
            messages.success(
                request, "Vendedor editado correctamente", extra_tags="exito"
            )
            return redirect("vendedores")
        else:
            alertas = None
            for field, errores in formulario.errors.items():
                alertas = errores[0]
                break
    else:
        formulario = VendedorForm(instance=vendedor)
        alertas = None
    return render(
        request,
        "vendedores/editar.html",
        {
            "titulo": "Editar vendedor",
            "formulario": formulario,
            "alertas": alertas,
            "vendedor": vendedor,
        },
    )


def eliminar(request):
    if request.method == "POST":
        try:
            id = int(request.POST.get("id"))
            vendedor = Vendedor.objects.get(pk=id)
        except ValueError:
            messages.error(request, "ID del vendedor inválido", extra_tags="error")
        except TypeError:
            messages.error(
                request, "Tipo de dato incorrecto para el ID", extra_tags="error"
            )
        except Vendedor.DoesNotExist:
            messages.error(request, "Vendedor no encontrado", extra_tags="error")
        else:
            if Propiedad.objects.filter(vendedor=vendedor).exists():
                messages.error(
                    request,
                    "El vendedor está enlazado a una propiedad",
                    extra_tags="error",
                )
            else:
                vendedor.delete()
                messages.success(
                    request, "Vendedor eliminado correctamente", extra_tags="exito"
                )
        return redirect("vendedores")
    else:
        messages.error(request, "Petición no válida", extra_tags="error")
        return redirect("vendedores")
