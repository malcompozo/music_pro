from django.contrib import admin
from .models import Products, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created', 'updated')
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created', 'updated')

admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

