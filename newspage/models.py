from django.db import models

class Sources(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    name = models.CharField(max_length=35,)
    description = models.CharField(max_length=37)
    url = models.URLField()
    category = models.CharField(max_length=100)
    country = models.CharField(max_length=12)
    language = models.CharField(max_length=16)


class Articles(models.Model):
    id = models.CharField(max_length=47,primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    url=models.URLField()
    image=models.ImageField()
    date= models.DateField()

