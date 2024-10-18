# Create your models here.
from django.db import models

class Producto(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion