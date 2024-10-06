from django.urls import path
from . import views

urlpatterns = [
    path("crear/", views.crear, name="crear_propiedad"),
    path("editar/<int:id>/", views.editar, name="editar_propiedad"),
    path("eliminar/", views.eliminar, name="eliminar_propiedad"),
]
