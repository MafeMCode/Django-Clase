from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60)
    cuerpo = models.TextField()
    fpublicacion = models.DateField(default='2024-07-22')
    
    def __str__(self):
        return self.titulo