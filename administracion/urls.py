from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="administracion"),
    path("propiedades/", include("propiedades.urls")),
    path("vendedores/", include("vendedores.urls")),
]
