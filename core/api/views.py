from services.models import Productos
from .serializers import UserSerializer, GroupSerializer, ProductoSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group

@api_view(['GET', 'POST'])
def get_products (request):
    if request.method == 'GET':
        producto = Productos.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        de_serializer = ProductoSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def get_products_id (request, pk):
    if request.method == 'GET':
        producto = Productos.objects.get(pk=pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    if request.method == 'PUT': 
        producto = Productos.objects.get(pk=pk)
        de_serializer = ProductoSerializer(producto, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)
           
    if request.method == 'DELETE':     
        producto = Productos.objects.get(pk=pk)
        producto.delete()
        data={"result":True}
        return Response(data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]