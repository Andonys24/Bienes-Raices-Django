from django.db import models
from django.utils.html import mark_safe
from vendedores.models import Vendedor
from .context_processors import get_unique_filename


class Propiedad(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(
        upload_to=get_unique_filename,
        verbose_name="Imagen",
    )
    descripcion = models.TextField(max_length=1000)
    habitaciones = models.IntegerField()
    wc = models.IntegerField()
    estacionamientos = models.IntegerField()
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_imagen = Propiedad.objects.get(pk=self.pk).imagen
            if old_imagen and old_imagen != self.imagen:
                old_imagen.delete(save=False)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.imagen:
            self.imagen.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo

    def imagen_thumbnail(self):
        if self.imagen:
            return mark_safe(f'<img src="{self.imagen.url}" width="50" height="50" />')
        return "No Image"

    imagen_thumbnail.short_description = "Imagen"
