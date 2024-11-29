from django.db import models

# Create your models here.
   
class Autor(models.Model):
    nombre = models.CharField(max_length=60, verbose_name="Nombre")
    apellidos = models.CharField(max_length=60, verbose_name="Apellidos")
    email = models.EmailField(unique=True, max_length=200, verbose_name="Email")
    dni = models.CharField(unique=True, max_length=9, verbose_name="Dni")
    bio = models.TextField(blank=True, verbose_name="Biografía")
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fpublicacion = models.DateField(default='2024-07-22')
    
    def __str__(self):
        return self.titulo