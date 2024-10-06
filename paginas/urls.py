from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("anuncios/", views.anuncios, name="anuncios"),
    path("anuncio/<int:id>", views.anuncio, name="anuncio"),
    path("blog/", views.blog, name="blog"),
    path("entrada/", views.entrada, name="entrada"),
    path("contacto/", views.contacto, name="contacto"),
]
