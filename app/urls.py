from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('videojuego/<str:titulo>/sede/<str:pais>', views.titulo_pais, name="titulo_pais"),
        path('plataforma/<str:fabricante>/plataforma/<str:nombre>/analisis/<int:puntuacion>', views.plataforma_analisis, name="plataforma_analisis")
]
