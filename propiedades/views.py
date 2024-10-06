from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Propiedad
from vendedores.models import Vendedor
from .forms import PropiedadForm


# Create your views here.
def crear(request):
    vendedores = Vendedor.objects.all()
    if request.method == "POST":
        formulario = PropiedadForm(request.POST, request.FILES)
        if formulario.is_valid():
            propiedad = formulario.save(commit=False)
            propiedad.save()
            messages.success(
                request, "Propiedad creada correctamente", extra_tags="exito"
            )
            return redirect("administracion")
        else:
            alertas = None
            # Mostrar solo una alerta
            for field, errores in formulario.errors.items():
                alertas = errores[0]
                break
    else:
        formulario = PropiedadForm()
        alertas = None
    return render(
        request,
        "propiedades/crear.html",
        {
            "titulo": "Crear Propiedad",
            "formulario": formulario,
            "vendedores": vendedores,
            "alertas": alertas,
        },
    )


def editar(request, id):
    if id is None or type(id) != int:
        return redirect("administracion")

    try:
        propiedad = Propiedad.objects.get(pk=id)
    except Propiedad.DoesNotExist:
        return redirect("administracion")

    vendedores = Vendedor.objects.all()
    if request.method == "POST":
        formulario = PropiedadForm(request.POST, request.FILES, instance=propiedad)
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request, "Propiedad actualizada correctamente", extra_tags="exito"
            )
            return redirect("administracion")
        else:
            alertas = None
            # Mostrar solo una alerta
            for field, errores in formulario.errors.items():
                alertas = errores[0]
                break
    else:
        formulario = PropiedadForm(instance=propiedad)
        alertas = None
    return render(
        request,
        "propiedades/editar.html",
        {
            "titulo": propiedad.titulo,
            "propiedad": propiedad,
            "formulario": formulario,
            "vendedores": vendedores,
            "alertas": alertas,
        },
    )


def eliminar(request):
    if request.method == "POST":
        try:
            id = int(request.POST.get("id"))
            propiedad = Propiedad.objects.get(pk=id)
        except ValueError:
            messages.error(
                request, "ID de propiedad no válido", extra_tags="error"
            )
        except TypeError:
            messages.error(
                request, "Tipo de dato incorrecto para el ID de propiedad", extra_tags="error"
            )
        except Propiedad.DoesNotExist:
            messages.error(
                request, "La propiedad con el ID proporcionado no existe", extra_tags="error"
            )
        else:
            # propiedad.delete()
            print(f"{propiedad}")
            messages.success(
                request, "Propiedad eliminada correctamente", extra_tags="exito"
            )
        return redirect("administracion")
    else:
        messages.error(request, "Método de solicitud no permitido para eliminar la propiedad", extra_tags="error")
        return redirect("administracion")
