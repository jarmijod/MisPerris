from django.db import models

class Mascota(models.Model):
     nombreMascota=models.CharField(max_length=20)
    razaMascota=models.CharField(max_length=50)
# Create your models here.
