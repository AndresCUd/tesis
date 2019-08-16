from django.db import models

# Create your models here.
class lista(models.Model):
    archivo =models.FileField(upload_to='datos/',null=True,blank=True)
    tamano = models.IntegerField(default=0)
    nombre =models.TextField(max_length=200,blank=True)


class nodos(models.Model):
   #Lora
   EstadoLora =models.BooleanField(default=False)
   NumeroNodo = models.IntegerField(default = 0)
   AnchoBanda = models.IntegerField(default = 0)
   Corriente = models.IntegerField(default = 0)
   PaquetesEnviados = models.IntegerField(default = 0)
   PaquetesRecibidos = models.IntegerField(default = 0)
   TiempoEnvio = models.IntegerField(default = 0)
   FuerzaSenal = models.IntegerField(default = 0)
   CargaUtil = models.IntegerField(default = 0)
   #GNSS
   estadoGnss = models.BooleanField(default=False)
   NumeroSatelites = models.IntegerField(default = 0)
   dilucion = models.IntegerField(default= 0)
   latitud =  models.IntegerField(default=0)
   longitud = models.IntegerField(default=0)
   altitud = models.IntegerField(default=0)
   fixQuality=models.IntegerField(default=0)
  
