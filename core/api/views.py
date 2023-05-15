from services.models import Productos
from .serializers import UserSerializer, GroupSerializer, ProductoSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group

@api_view(['GET', 'POST'])
def get_products (request):
    if request.method == 'GET':
        try:
            producto = Productos.objects.all()
            serializer = ProductoSerializer(producto, many=True)
            return Response(serializer.data)
        except Productos.DoesNotExist:
            return Response({'ERROR': 'NO EXISTEN PRODUCTOS INGRESADOS'}, status=status.HTTP_404_NOT_FOUND) # no encontrado
    
    if request.method == 'POST':
        de_serializer = ProductoSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST) # envio de tipo de dato erroneo

@api_view(['GET', 'PUT', 'DELETE'])
def get_products_id (request, pk):
    if request.method == 'GET':
        try:
            producto = Productos.objects.get(pk=pk)
            serializer = ProductoSerializer(producto)
            return Response(serializer.data)
        except Productos.DoesNotExist:
            return Response({'ERROR': 'NO EXISTEN PRODUCTOS CON ESE ID'}, status=status.HTTP_404_NOT_FOUND) # no encontrado
    
    if request.method == 'PUT': 
        producto = Productos.objects.get(pk=pk)
        de_serializer = ProductoSerializer(producto, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST) # envio de tipo de dato erroneo
           
    if request.method == 'DELETE': 
        try:    
            producto = Productos.objects.get(pk=pk)
            producto.delete()
        except Productos.DoesNotExist:
            return Response({'ERROR':' El registro no existe'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]