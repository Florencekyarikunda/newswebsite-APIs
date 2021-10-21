from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=30,primary_key=True)