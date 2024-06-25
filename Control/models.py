from django.db import models

# Create your models here.
class Bitacora(models.Model):
    accion = models.CharField(max_length=200)
    fecha = models.DateField()

class Login(models.Model):
    usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    RUT = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=200)

class Boletas(models.Model):
    fecha = models.DateField


class Delivery(models.Model):
    precio = models.IntegerField()
    fecha = models.DateField()
    estado_entrega = models.BooleanField()

class Bodega(models.Model):
    fecha = models.DateField()

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=200)

