from django import forms
from django.core.exceptions import ValidationError
from .models import Vendedor
import re


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        exclude = ["creado", "actualizado"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"id": "nombre", "placeholder": "Ingrese el Nombre"}
            ),
            "apellido": forms.TextInput(
                attrs={"id": "apellido", "placeholder": "Ingrese el Apellido"}
            ),
            "telefono": forms.NumberInput(
                attrs={"id": "telefono", "placeholder": "Ingrese el Teléfono", "min": 0}
            ),
        }

        labels = {
            "nombre": "Nombre",
            "apellido": "Apellido",
            "telefono": "Teléfono",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def validar_string(self, valor, limite_min, limite_max, campo):
        valor = self.cleaned_data.get(valor)
        if not valor:
            raise ValidationError(f"Este {campo} es requerido")
        if len(valor) > limite_max:
            raise ValidationError(
                f"El {campo} debe tener menos de {limite_max} caracteres"
            )
        if len(valor) < limite_min:
            raise ValidationError(
                f"El {campo} debe tener más de {limite_min} caracteres"
            )
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$", valor):
            raise ValidationError(
                f"El {campo} solo puede contener letras sin espacios ni números"
            )
        return valor.strip()

    def clean_nombre(self):
        return self.validar_string("nombre", 2, 60, "nombre")

    def clean_apellido(self):
        return self.validar_string("apellido", 2, 60, "apellido")

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono")
        if not telefono:
            raise ValidationError("Este teléfono es requerido")
        if len(telefono) > 15:
            raise ValidationError("El teléfono debe tener menos de 15 caracteres")
        if len(telefono) < 8:
            raise ValidationError("El teléfono debe tener más de 8 caracteres")
        if not re.match(r"^\d+$", telefono):
            raise ValidationError("El teléfono solo puede contener números")
        return telefono.strip()
