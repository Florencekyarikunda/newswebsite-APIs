from django.urls import path
from .import views

app_name='newspage'



urlpatterns=[
        path('', views.home, name="home"),
        path("articles/",views.articles,name="articles"),
        # path("sources/",views.sources,name="sources"),
        # path("register", views.register_request, name="register")

        ]
