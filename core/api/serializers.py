from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductoSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)
    nom_producto = serializers.CharField()
    subtitle = serializers.CharField()
    descripcion = serializers.CharField()
    image = serializers.ImageField()
    value = serializers.IntegerField() 
    created = serializers.DateTimeField ()
    updated = serializers.DateTimeField ()
