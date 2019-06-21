from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Modelo.models import Registro
from Modelo.models import Alumno

from Modelo.serializer import RegistroSerializers
from Modelo.serializer import AlumnoSerializers

class RegistroList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Registro.objects.filter(delete = False) #id.example2=id.example (en caso de llaves foraneas)
        #many = True Si aplica si retorno multiples objetos
        serializer = RegistroSerializers(queryse, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RegistroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.error, status = status.HTTP_404_BAD_REQUEST)
        
class RegistroDetail(APIView):
    def get_object(self, id):
        try:
            return Registro.objects.get(pk=id, delete=False)
        except Registro.DoesNotExist:
            return 404

    def get(self, id, request, format = None):
        registro = self.get_object(id)
        if registro != 404:
            serializer = RegistroSerializers(registro)
            return Response(seralizer.data)
        else:
            return Response(registro)
    
    def put(self, request, id, format=None):
        registro = self.get_object(id)
        if registro != 404:
            serializer = ExampleSerializers(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

class AlumnoList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delete = False)
        serializer = AlumnoSerializers(queryset)
        return Response(serializer.data)


