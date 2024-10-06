from django import forms
from django.core.exceptions import ValidationError
from .models import Propiedad
import re


class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        exclude = ["creado", "actualizado"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "id": "titulo",
                    "placeholder": "Ingrese el Título",
                }
            ),
            "precio": forms.NumberInput(
                attrs={
                    "id": "precio",
                    "placeholder": "Ingrese el Precio",
                    "min": 0,
                }
            ),
            "imagen": forms.ClearableFileInput(
                attrs={
                    "id": "imagen",
                    "accept": "image/jpeg, image/png",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "id": "descripcion",
                    "placeholder": "Ingrese la Descripción",
                }
            ),
            "habitaciones": forms.NumberInput(
                attrs={
                    "id": "habitaciones",
                    "placeholder": "Ingrese la Cantidad de Habitaciones",
                    "min": 0,
                }
            ),
            "wc": forms.NumberInput(
                attrs={
                    "id": "wc",
                    "placeholder": "Ingrese la Cantidad de Baños",
                    "min": 0,
                }
            ),
            "estacionamientos": forms.NumberInput(
                attrs={
                    "id": "estacionamientos",
                    "placeholder": "Ingrese la Cantidad de Estacionamientos",
                    "min": 0,
                }
            ),
            "vendedor": forms.Select(
                attrs={
                    "id": "vendedor",
                }
            ),
        }

        labels = {
            "titulo": "Título",
            "precio": "Precio",
            "imagen": "Imagen",
            "descripcion": "Descripción",
            "habitaciones": "Habitaciones",
            "wc": "Baños",
            "estacionamientos": "Estacionamientos",
            "vendedor": "Vendedor",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def clean_titulo(self):
        titulo = self.cleaned_data.get("titulo")
        if not titulo:
            raise ValidationError("El campo del título no puede estar vacío")
        if len(titulo) < 10:
            raise ValidationError("El título debe tener al menos 10 caracteres")
        if len(titulo) > 200:
            raise ValidationError("El título no puede tener más de 200 caracteres")
        if not re.match(r"^[\w\s]+$", titulo):
            raise ValidationError("El título solo puede contener letras y números")
        return titulo.strip()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        if not descripcion:
            raise ValidationError("El campo de la descripción no puede estar vacío")
        if len(descripcion) < 150:
            raise ValidationError("La descripción debe tener al menos 150 caracteres")
        if len(descripcion) > 1000:
            raise ValidationError(
                "La descripción no puede tener más de 1000 caracteres"
            )
        return descripcion.strip()

    def clean_imagen(self):
        imagen = self.cleaned_data.get("imagen")
        if not imagen or imagen == "null":
            raise ValidationError("Debe seleccionar una imagen")
        return imagen

    def clean_field(self, field_name, field_label):
        field_value = self.cleaned_data.get(field_name)
        if field_value is None:
            raise ValidationError(f"El campo de {field_label} no puede estar vacío")
        if field_value <= 0:
            raise ValidationError(
                f"La cantidad de {field_label} no puede ser negativa o cero"
            )
        return field_value

    def clean_precio(self):
        return self.clean_field("precio", "precio")

    def clean_habitaciones(self):
        return self.clean_field("habitaciones", "habitaciones")

    def clean_wc(self):
        return self.clean_field("wc", "baños")

    def clean_estacionamientos(self):
        return self.clean_field("estacionamientos", "estacionamientos")

    def clean_vendedor(self):
        vendedor = self.cleaned_data.get("vendedor")
        if not vendedor or vendedor == "null":
            raise ValidationError("Debe seleccionar un vendedor")
        return vendedor
