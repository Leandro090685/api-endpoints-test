from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests


def index(request):
    r = requests.get("http://ip-api.com/json/")
    datos = r.json()
    return JsonResponse(datos)

def current(request, city=None):
    if (not city):
        r = requests.get("http://ip-api.com/json/")
        datos = r.json()
        city = datos["city"]
        r2= requests.get("https://wttr.in/"+ city +"?format=j1&lang=es")
        datos2 = r2.json()
        return JsonResponse(datos2)
    else:
        r3= requests.get("https://wttr.in/"+ city +"?format=j1&lang=es")
        datos3 = r3.json()
        return JsonResponse(datos3)

def prueba(request):
    return HttpResponse("hola mundo")



    

