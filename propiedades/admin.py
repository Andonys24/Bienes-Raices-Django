from django.contrib import admin
from .models import Propiedad


# Register your models here.
class PropiedadAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion", "fecha_actualizacion")
    list_display = ("titulo", "precio", "vendedor", 'imagen_thumbnail')
    search_fields = (
        "titulo",
        "precio",
        "habitaciones",
        "wc",
        "estacionamientos",
        "vendedor",
    )
    ordering = ("-fecha_creacion",)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "imagen":
            formfield.widget.can_delete_related = False
        return formfield


admin.site.register(Propiedad, PropiedadAdmin)
