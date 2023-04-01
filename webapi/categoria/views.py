from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from webapi.models import Categoria
from webapi.serializers import CategoriaSerializer

@api_view(['POST'])
def crear_categoria(request):
    data = JSONParser().parse(request)
    serializer = CategoriaSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['PUT'])
def actualizar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(id=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    serializer = CategoriaSerializer(categoria, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
