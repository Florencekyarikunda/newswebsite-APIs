from django.contrib import admin

from news.App_Login.models import UserProfile
from .models import UserProfile


# Register your models here.
admin.site.register(UserProfile)