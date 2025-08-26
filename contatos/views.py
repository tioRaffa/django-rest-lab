from rest_framework import serializers
from contatos.models import ContatosModel
from contatos.serializer import ContatosSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
# Create your views here.


class ContatosAPIView(APIView):
    def get(self, request):
        contatos = ContatosModel.objects.all()

        name = request.query_params.get('name')
        if name:
            contatos = contatos.filter(name__icontains=name)
        
        phone = request.query_params.get('phone')
        if phone:
            contatos = contatos.filter(phone__icontains=phone)

        serializer = ContatosSerializer(contatos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ContatosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContatoAPIView(APIView):
    def get_object(self, pk):
        obj = get_object_or_404(ContatosModel, pk=pk)
        return obj

    def get(self, request, pk):
        contato = self.get_object(pk=pk)
        serializer = ContatosSerializer(contato)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        contato = self.get_object(pk=pk)
        serializer = ContatosSerializer(contato, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)