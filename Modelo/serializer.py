#Agregando librerias fram
from rest_framework import routers, serializers, viewsets

#Agregando modelos
from Modelo.models import Registro
from Modelo.models import Alumno

class RegistroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ('__all__')

class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('__all__')