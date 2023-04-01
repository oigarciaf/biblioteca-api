from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    codigo_categoria = models.CharField(max_length=50)
    num_libros = models.IntegerField()

    def __str__(self):
        return self.nombre + " "+ self.codigo_categoria + " " + self.numero_libros
        
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    ejemplares = models.IntegerField()
    pais = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    premios = models.TextField()

    def __str__(self):
        return self.nombre 
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    responsable = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
class Libro(models.Model):
    codigo = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    editorial = models.CharField(max_length=50)
    pais_libro = models.CharField(max_length=50)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    edicion = models.CharField(max_length=50)
    ejemplares = models.IntegerField()
    ubicacion = models.CharField(max_length=50)
    adquirido = models.CharField(max_length=50)
    valor_estimado = models.DecimalField(max_digits=8, decimal_places=2)
    resumen = models.TextField()
    
    def __str__(self):
        return self.titulo +" " + self.autor +" "+ self.categoria