from django.db import models

# Create your models here.
class lista(models.Model):
    archivo =models.FileField(upload_to='datos/',null=True,blank=True)
    tamano = models.IntegerField(default=0)
    nombre =models.TextField(max_length=200,blank=True)


class nodos(models.Model):
    nombre = models.TextField(max_length=200,blank=True)
    estado = models.BooleanField(default=False)
    fixQuality =models.IntegerField(default=0)
    satelites =models.IntegerField(default = 0)
    latitud = models.TextField(max_length =200,blank=True)
    longitud = models.TextField(max_length =200,blank=True)
    altitud = models.IntegerField(default = 0)
    latencia = models.IntegerField(default = 0)
    frecuencia =models.IntegerField(default = 0)
    power =models.IntegerField(default = 0)
    CRC =models.BooleanField(default=False)