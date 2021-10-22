from django.db import models
from django.contrib.auth.models import User


class Sources:
    '''
    Sources class to define Sources Objects
    '''
    user = models.ForeignKey(
            User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language


class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date 

