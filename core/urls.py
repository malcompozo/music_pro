from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    #path del core
    path('', views.home, name= "home"),
    path('about/', views.about, name= "about"),
    path('store/', views.store, name= "store"),
    path('contact/', views.contact, name= "contact"),
    path('sample/', views.sample, name= "sample"),
    #path de admin djangoRest
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


