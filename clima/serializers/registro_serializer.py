from rest_framework import serializers
from clima.models import Registros
import requests

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registros
        fields = "__all__"
    