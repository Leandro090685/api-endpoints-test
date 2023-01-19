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
        final = {
            "Ciudad": datos2["nearest_area"][0]["region"][0]["value"],
            "Temperatura": datos2["current_condition"][0]["FeelsLikeC"]+"º",
            "Humedad" : datos2["current_condition"][0]["humidity"]+" %",
            "Sensacion Termica": datos2["weather"][0]["hourly"][0]["FeelsLikeC"]+"º",
            }
        return JsonResponse(final)
    else:
        r3= requests.get("https://wttr.in/"+ city +"?format=j1&lang=es")
        datos3 = r3.json()
        final2 = {
            "Ciudad": datos3["nearest_area"][0]["region"][0]["value"],
            "Temperatura": datos3["current_condition"][0]["FeelsLikeC"]+"º",
            "Humedad" : datos3["current_condition"][0]["humidity"]+" %",
            "Sensacion Termica": datos3["weather"][0]["hourly"][0]["FeelsLikeC"]+"º",
            }
        return JsonResponse(final2)
        

def prueba(request):
    return HttpResponse("hola mundo")
    

