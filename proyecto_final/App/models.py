from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pantalon(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    marca = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nombre}"

class Zapatilla(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    marca = models.CharField(max_length=45)


    def __str__(self):
        return f"{self.nombre}"

class Gorra(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    marca = models.CharField(max_length=45)


    def __str__(self):
        return f"{self.nombre}"


class Remera(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    marca = models.CharField(max_length=45)


    def __str__(self):
        return f"{self.nombre}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"