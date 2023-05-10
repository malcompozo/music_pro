from django.shortcuts import render
from .models import Productos

# Create your views here.
def services(request):
        services = Productos.objects.all()
        return render(request, "services/services.html",{'products':services})