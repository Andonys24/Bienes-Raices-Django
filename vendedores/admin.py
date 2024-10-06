from django.contrib import admin
from .models import Vendedor


# Register your models here.
class vendedorAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion", "fecha_actualizacion")
    list_display = ("nombre", "apellido", "telefono")
    search_fields = ("nombre", "apellido", "telefono")
    ordering = ("-fecha_actualizacion",)


admin.site.register(Vendedor, vendedorAdmin)
