from rest_framework import serializers
from django.contrib.auth.models import User, Group
from services.models import Productos, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nom_category = serializers.CharField()
    description = serializers.CharField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nom_category = validated_data.get('nom_producto', instance.nom_producto)
        instance.description = validated_data.get('descripcion', instance.descripcion)
        instance.save()
        return instance
    
    class Meta:
        model = Category
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nom_producto = serializers.CharField()
    subtitle = serializers.CharField()
    descripcion = serializers.CharField()
    image = serializers.CharField()
    value = serializers.IntegerField() 
    created = serializers.DateTimeField ()
    updated = serializers.DateTimeField ()
    categoria = CategorySerializer(many=True, read_only=True) 
    #categoria = serializers.StringRelatedField() 

    def create(self, validated_data):
        return Productos.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nom_producto = validated_data.get('nom_producto', instance.nom_producto)
        instance.subtitle = validated_data.get('subtitle', instance.subtitle)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.image = validated_data.get('image', instance.image)
        instance.value = validated_data.get('value', instance.value)
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.save()
        return instance
    
    class Meta:
        model = Productos
        fields = '__all__'
