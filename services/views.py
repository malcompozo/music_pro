from django.shortcuts import render
from datetime import datetime, date, time, timedelta
import requests

# Create your views here.
def products(request):
        url = 'http://localhost:8000/api/productos'  # URL de la API en localhost
        response = requests.get(url)

        if response.status_code == 200:
                products = response.json()  # Obtener los datos de la respuesta en formato JSON
                print(products)
                return render(request, "services/services.html",{'products':products})
        
        else:
                error_msg = f"Error al consumir la API: {response.status_code}"
                return render(request, "services/services.html",{'error':error_msg})

def apis(request):
        arrayData = {}
        urlCmf = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar?apikey=02f0f7e74d22234ae406894dddbc6158bb66b8ab&formato=json'  # URL CMF
        responseCmf = requests.get(urlCmf)
        urlProd = 'http://localhost:8000/api/productos'  # URL de la API en localhost
        responseProd = requests.get(urlProd)

        if responseCmf.status_code == 200:
                cmf = responseCmf.json()  # Obtener los datos de la respuesta en formato JSON
                arrayData['cmf'] = cmf
        else:
                diasMenos = 1
                successResponse = False
                while successResponse == False:
                        fecha_actual = datetime.now()
                        # Restar un día utilizando timedelta
                        un_dia = timedelta(days=diasMenos)
                        fecha_anterior = fecha_actual - un_dia
                        annio = fecha_anterior.year
                        mes = fecha_anterior.month
                        dia = fecha_anterior.day
                        urlCmfRecupero = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/'+str(annio)+'/'+str(mes)+'/dias/'+str(dia)+'?apikey=02f0f7e74d22234ae406894dddbc6158bb66b8ab&formato=json'
                        responseCmfRecupero = requests.get(urlCmfRecupero)

                        if responseCmfRecupero.status_code == 200:
                                cmf = responseCmfRecupero.json()
                                arrayData['cmf'] = cmf
                                successResponse = True
                        else:
                                error_msg = f"Error al consumir la API: {responseCmf.status_code}"
                                diasMenos += 1
        
        if responseProd.status_code == 200:
                products = responseProd.json() # Obtener los datos de la respuesta en form
                arrayData['products'] = products
        else:
                error_msg = f"Error al consumir la API: {responseCmf.status_code}"
                return render(request, "services/services.html",{'error':error_msg})

        return render(request, "services/services.html",arrayData)