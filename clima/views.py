from clima.models import Registros
from rest_framework import generics,status
from rest_framework.response import Response 
from rest_framework.views import APIView
from clima.serializers.registro_serializer import RegistroSerializer
from clima.services.service_register import RegisterService


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