from django.urls import re_path
from webapi.libro.views import libro_list, libro_detail
from webapi.categoria.views import crear_categoria, listar_categorias, actualizar_categoria
from webapi.autor.views import autor_detail, autor_list
from webapi.proveedor.views import proveedor_detail, proveedor_list

urlpatterns = [

    #Categoria 
    re_path(r'^api/crear-categoria/$', crear_categoria),
    re_path(r'^api/listar-categorias/$', listar_categorias),
    re_path(r'^api/actualizar-categoria/(?P<id>[0-9]+)/$', actualizar_categoria),

    #Autor
    re_path(r'^api/autores/$', autor_list),
    re_path(r'^api/autores/(?P<pk>[0-9]+)/$', autor_detail),

    #re_path(r'^api/autores/$', autor_list),
    #re_path(r'^api/autores/(?P<pk>[0-9]+)/$', autor_detail),
    #Proveedor
    re_path(r'^api/proveedores/$', proveedor_list),
    re_path(r'^api/proveedores/(?P<pk>[0-9]+)/$', proveedor_detail),

    #Libro
    re_path(r'^api/libros/$', libro_list),
    re_path(r'^api/libros/(?P<pk>[0-9]+)/$', libro_detail)
]
