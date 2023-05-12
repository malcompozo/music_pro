from django.shortcuts import render
from .models import Productos

# Create your views here.
def products(request):
        products = Productos.objects.all()
        return render(request, "services/services.html",{'products':products})