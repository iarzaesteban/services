from django.db import models
from applications.users.models import User
from applications.clients.models import Client

class Chat(models.Model):
    TIPOS = (
        ('texto', 'Texto'),
        ('imagen', 'Imagen'),
        ('video', 'Video'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mensaje = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    multimedia = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.mensaje
