from django.db import models
from applications.users.models import User

class ImagenTrabajo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    url_imagen = models.CharField(max_length=255)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    resolucion = models.CharField(max_length=20)

    def __str__(self):
        return self.url_imagen
