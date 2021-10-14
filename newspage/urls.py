from django.urls import path
from newspage.models import Articles
from .views import Articles

urlpatterns=[
        path("",Articles,name="newspage"),
        path("newspage/",Articles,name="Articles"),
        ]
