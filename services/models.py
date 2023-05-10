from django.db import models

# Create your models here.
class Productos(models.Model):
    #id = models.IntegerField(read_only=True)
    nom_producto = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    descripcion = models.CharField(max_length=500,verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    value = models.IntegerField(verbose_name='Valor') 
    created = models.DateTimeField (auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField (auto_now=True, verbose_name='Actualización')

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['-created']

    def __str__(self):
        return self.nom_producto