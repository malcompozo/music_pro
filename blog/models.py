from django.db import models
# importar la zona horaria actual
from django.utils.timezone import now
# importar claves foraneas
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField (auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField (auto_now=True, verbose_name='Actualización')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Titulo')
    content = models.TextField(verbose_name ='Contenido')
    published = models.DateTimeField(verbose_name ='Fecha de publicación',default = now)
    image = models.ImageField(verbose_name='imagen',null = True, blank = True)
    # Campo de autor donde hereda foreingkey
    author = models.ForeignKey(User, verbose_name='Autor',on_delete = models.CASCADE)
    # campo categoria donde se pueden elegir muchas categorias 
    categories = models.ManyToManyField(Category,verbose_name='Categorías')
    created = models.DateTimeField (auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField (auto_now=True, verbose_name='Actualización')

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title