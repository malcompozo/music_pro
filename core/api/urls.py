from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    #path de admin djangoRest
    path('', include(router.urls)),
    path('productos/', views.get_products, name='productos' ),
    path('productos/<int:pk>', views.get_products_id, name='productos_id' ),
    path('categoria/', views.get_categories, name='productos' ),
    path('categoria/<int:pk>', views.get_category_id, name='productos_id' ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]