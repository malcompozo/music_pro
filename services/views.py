from django.shortcuts import render
import requests

# Create your views here.
def products(request):
        url = 'http://localhost:8000/api/productos'  # URL de la API en localhost
        response = requests.get(url)

        if response.status_code == 200:
                products = response.json()  # Obtener los datos de la respuesta en formato JSON
                return render(request, "services/services.html",{'products':products})
        
        else:
                error_msg = f"Error al consumir la API: {response.status_code}"
                return render(request, "services/services.html",{'error':error_msg})
