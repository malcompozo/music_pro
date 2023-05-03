from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

    # personalizacion de entradas

    # mostrar campos en previsualizacion
    list_display = ('title', 'author', 'published','post_categories')

    """ 
        extender campos en previsualizacion
        crear un campor def nombre_funcion (self,obj) y todo el contenido que esta abajo
        luego pasar a list_display el nombre de esa funcion
    """
    # ordenar
    ordering = ('author','published')

    # Barra de busqueda
    search_fields = ('title', 'content','author__username','categories__name')

    # gerarquia de fechas
    date_hierarchy = 'published'

    # filtrado por campos
    list_filter = ('author__username','categories__name')

    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

