from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from clima.models import Registros
from django.forms.models import model_to_dict


def index(request):
    r = requests.get("http://ip-api.com/json/")
    datos = r.json()
    return JsonResponse(datos)

def current(request, city=None):

    while (not city):
        r = requests.get("http://ip-api.com/json/")
        city = r.json()["city"]

    r= requests.get("https://wttr.in/"+ city +"?format=j1&lang=es")
    data= r.json()

    registro = Registros()

    registro.city = city
    registro.temperature = data["current_condition"][0]["temp_C"]
    registro.humidity = data["current_condition"][0]["humidity"]
    registro.feels_like = data["current_condition"][0]["FeelsLikeC"]

    registro.save()
    return JsonResponse(model_to_dict(registro))

def prueba(request):
    return HttpResponse("hola mundo")
    


def delete(request):
    Registros.objects.all().delete()
    return HttpResponse("ok")
    
def find_all(request):
    all = Registros.objects.all()
    print("ACA ABAJO")
    lista = list()
    for one in all:
        lista.append(model_to_dict(one))
    final_dict = {"all_registers":lista}
    return JsonResponse(final_dict)
    
    