from rest_framework import serializers
from webapi.models import Categoria, Autor, Proveedor, Libro

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields =('id','nombre', 'codigo_categoria', 'num_libros')

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields =('id','nombre', 'ejemplares','pais', 'fecha_nacimiento', 'premios' )

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields =('id','nombre', 'email', 'direccion', 'telefono', 'responsable')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields =('id','codigo', 'titulo', 'id_autor', 'id_categoria', 
                 'editorial', 'pais_libro', 'id_proveedor', 'edicion','ejemplares', 
                 'ubicacion', 'adquirido', 'valor_estimado', 'resumen' )

