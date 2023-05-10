from services.models import Productos
from .serializers import UserSerializer, GroupSerializer, ProductoSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group

@api_view()
def get_products (request):
    producto = Productos.objects.all()
    serializer = ProductoSerializer(producto, many=True)
    return Response(serializer.data)

@api_view()
def get_products_id (request, pk):
    producto = Productos.objects.get(pk=pk)
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]