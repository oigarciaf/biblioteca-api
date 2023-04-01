from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from webapi.models import Libro
from webapi.serializers import LibroSerializer

@api_view(['GET', 'POST'])
def libro_list(request):
    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def libro_detail(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    elif request.method == 'DELETE':
        libro.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
