from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)  # Campo para cargar imagen

    def __str__(self):
        return self.titulo