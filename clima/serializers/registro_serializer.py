from rest_framework import serializers
from clima.models import Registros

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registros
        fields = "__all__"
    
    def create(self):
        