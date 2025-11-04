from django.db import models

# Create your models here.

class Plataforma(models.Model):
    nombre = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=30)

class Sede(models.Model):
    pais = models.CharField(max_length=20)
    
class Estudio(models.Model):
    nombre = models.CharField(max_length=30)
    sede = models.OneToOneField(Sede, on_delete=models.CASCADE)
    
class Videojuego(models.Model):
    titulo = models.CharField(max_length=50)
    plataforma = models.ManyToManyField(Plataforma)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)

class Analisis(models.Model):
    puntuacion = models.IntegerField()
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)


