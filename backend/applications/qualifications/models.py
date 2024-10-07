from django.db import models
from applications.users.models import User
from applications.clients.models import Client

class qualifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    punctuation = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Calificación {self.punctuation} de {self.client} a {self.user}"
