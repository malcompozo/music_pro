from services.models import Products, Category
from .serializers import UserSerializer, GroupSerializer, ProductsSerializer, CategorySerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView



################################# PRODUCTO #################################
class ProductsListView(APIView):

    # GET /products
    def get(self, request):
        try:
            producto = Products.objects.all()
            serializer = ProductsSerializer(producto, many=True)
            return Response(serializer.data)
        except Products.DoesNotExist:
            return Response({'ERROR':' El registro no existe'}, status=status.HTTP_404_NOT_FOUND)

    # POST /products    
    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsDetailView(APIView):

    # GET ID /products
    def get(self, request, pk):
        try:
            producto = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Response({'ERROR':' El registro no existe'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductsSerializer(producto)
        return Response(serializer.data)

    # PUT ID /products
    def put(self, request, pk):
        try:
            producto = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Response({'ERROR ':' El registro no existe'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductsSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):  
        try:    
            producto = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Response({'ERROR ':' El registro no existe'}, status=status.HTTP_404_NOT_FOUND)
        
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


################################# CATEGORIA #################################
class CategoryListView(APIView):

    # GET /products
    def get(self, request):
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'ERROR':' El registro no existe'}, status=status.HTTP_404_NOT_FOUND)

    # POST /products    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    # GET ID /products
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'ERROR':' El registro no existe'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    # PUT ID /products
    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'ERROR ':' El registro no existe'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):  
        try:    
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'ERROR ':' El registro no existe'}, status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


################################# USUARIO #################################
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

################################# GRUPOS #################################
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
