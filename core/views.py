from django.shortcuts import render
from .serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group

# Create your views here.
def home(request):
        return render(request, "core/home.html")

def about(request):
        return render(request, "core/about.html")

def store(request):
        return render(request, "core/store.html")

def contact(request):
        return render(request, "core/contact.html")

def sample(request):
        return render(request, "core/sample.html")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]