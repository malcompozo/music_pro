from rest_framework import serializers
from django.contrib.auth.models import User, Group
from services.models import Products, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        exclude = ['created', 'updated']

class CategorySerializer(serializers.ModelSerializer):
    categoria = ProductsSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        exclude = ['created', 'updated']




