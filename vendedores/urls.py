from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="vendedores"),
    path("agregar/", views.agregar, name="agregar_vendedor"),
    path("editar/<int:id>/", views.editar, name="editar_vendedor"),
    path("eliminar/", views.eliminar, name="eliminar_vendedor"),
]
