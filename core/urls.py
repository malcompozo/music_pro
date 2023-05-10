from django.urls import path, include
from . import views


urlpatterns = [
    #path del core
    path('', views.home, name= "home"),
    path('about/', views.about, name= "about"),
    path('store/', views.store, name= "store"),
    path('contact/', views.contact, name= "contact"),
    path('sample/', views.sample, name= "sample"),
    #path de admin djangoRest
    path('api/', include('core.api.urls')),
]


