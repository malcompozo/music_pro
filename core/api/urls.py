from django.urls import path, include
from .views import ProductsListView, ProductsDetailView, CategoryDetailView, CategoryListView, UserViewSet, GroupViewSet
from rest_framework import routers
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Music PRO API",
      default_version='v1',
      description="Documentation",
      terms_of_service="https://github.com/malcompozo/music_pro",
      #contact=openapi.Contact(email="contact@snippets.local"),
      #license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    #path de admin djangoRest
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('productos/', ProductsListView.as_view(), name='productos' ),
    path('productos/<int:pk>/', ProductsDetailView.as_view(), name='productos_id' ),
    path('categoria/', CategoryListView.as_view(), name='categoria' ),
    path('categoria/<int:pk>/', CategoryDetailView.as_view(), name='categoria_id' ),
    
]