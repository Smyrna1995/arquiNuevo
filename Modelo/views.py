from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from rest_framework import generics

from Modelo.models import Registro

from Modelo.serializer import RegistroSerializers

class RegistroList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None);
        queryset = Registro.objects.filter(delete=False)
        serializer = RegistroSerializers(queryset)
        return Response(serializer.data)
        
