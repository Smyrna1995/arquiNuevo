#Agregando librerias fram
from rest_framework import routers, serializers, viewsets

#Agregando modelos
from Modelo.models import Registro

class RegistroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ('__all__')
        