from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from clima.models import Registros
from django.forms.models import model_to_dict
from rest_framework import generics,status
from rest_framework.response import Response 
from rest_framework.views import APIView
from clima.serializers.registro_serializer import RegistroSerializer
from clima.services.service_register import RegisterService

from django.views.decorators.csrf import csrf_exempt

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
    
class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registros.objects.all()
    serializer_class = RegistroSerializer

class RegistrosListview(generics.ListAPIView):
    queryset = Registros.objects.all()
    serializer_class = RegistroSerializer

class CreateRegistro(APIView):
    def get(self,request,city=None,format=None):
        data = RegisterService.register(city)
        serializer = RegistroSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            


def find_all(request):
    all = Registros.objects.all()
    lista = list()
    for one in all:
        lista.append(model_to_dict(one))
    final_dict = {"all_registers":lista}
    return JsonResponse(final_dict)
    
@csrf_exempt
def delete(request,id):
    if request.method == 'DELETE':
        Registros.objects.filter(id=id).delete()
        message = "Id Nº "+str(id)+" deleted"
    else:
        message = "Error in method"
    return HttpResponse(message)
