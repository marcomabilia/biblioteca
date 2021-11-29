from django.db import models
from uuid import uuid4

# Create your models here.

class Obras(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    autores = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    foto = models.CharField(max_length=200)

# Create your models here.
