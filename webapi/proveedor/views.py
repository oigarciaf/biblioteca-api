from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from webapi.models import Proveedor
from webapi.serializers import ProveedorSerializer


@api_view(['GET', 'POST'])
def proveedor_list(request):
    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def proveedor_detail(request, pk):
    try:
        proveedor = Proveedor.objects.get(pk=pk)
    except Proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(proveedor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
