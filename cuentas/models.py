from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPers(AbstractUser):
    telefono = models.PositiveIntegerField(null=True, blank=True)
    direccion = models.PositiveIntegerField(null=True, blank=True)