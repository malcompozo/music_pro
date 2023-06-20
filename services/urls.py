from django.urls import path
from . import views

urlpatterns = [
    #path del core
    path('', views.apis, name= "products"),
    #path('', views.apis, name= "cmf"),
]