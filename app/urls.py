from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('videojuego/<str:titulo>/sede/<str:pais>', views.titulo_pais, name="titulo_pais"),
]
