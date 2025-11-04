from django.shortcuts import render
from django.views.defaults import page_not_found
from .models import *
from django.db.models import Q

# Create your views here.

# Errores

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_400(request,exception=None):
    return render(request, 'errores/400.html',None,None,400)

def mi_error_403(request,exception=None):
    return render(request, 'errores/403.html',None,None,403)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)

# Index
def index(request):
    return render(request, 'app/index.html')

# Querys

def titulo_pais(request, titulo, pais):
    videojuego = Videojuego.objects.select_related('estudio').prefetch_related('plataforma')
    videojuego = videojuego.filter(titulo__contains=titulo, estudio__sede__pais__contains=pais)
    videojuego = videojuego.all()
    return render(request, 'app/titulo_pais.html', {'titulo_pais':videojuego})

def plataforma_analisis(request, fabricante, nombre, puntuacion):
    videojuego = Videojuego.objects.select_related('estudio').prefetch_related('plataforma')
    videojuego = videojuego.filter(Q(plataforma__fabricante=fabricante) | Q(plataforma__nombre__contains=nombre))
    videojuego = videojuego.filter(analisis__puntuacion__gt = puntuacion)[:3]
    videojuego = videojuego.all()
    return render(request, 'app/plataforma_analisis.html', {'plataforma_analisis':videojuego})

def ventas_estimadas(request):
    videojuego = Videojuego.objects.select_related('estudio').prefetch_related('plataforma')
    videojuego = videojuego.filter(videojuego_plataforma=None).order_by('ventas_estimadas')
    videojuego = videojuego.all()
    return render(request, 'app/ventas_estimadas.html', {'ventas_estimadas':videojuego})

def analisis_anyo(request, anyo):
    videojuego = Videojuego.objects.select_related('estudio')
    videojuego = videojuego.filter(analisis__fecha__year=anyo).order_by('-analisis__puntuacion')
    videojuego = videojuego.all()
    return render(request, 'app/analisis_anyo.html', {'analisis_anyo': videojuego})