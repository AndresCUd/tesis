from django.db import models

# Create your models here.
class lista(models.Model):
    archivo =models.FileField(upload_to='datos/',null=True,blank=True)
    tamano = models.IntegerField(default=0)
    nombre =models.TextField(max_length=200,blank=True)

    