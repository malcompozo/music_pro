from django.urls import path
from . import views

urlpatterns = [
    #path del core
    path('', views.products, name= "products"),
    #path('', views.apis, name= "cmf"),
]