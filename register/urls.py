from django.urls import path
from .import views


app_name = "newspage"   


urlpatterns = [
    path("newspage", views.NewUserForm, name="NewUserForm"),
    # path("register", views.register_request, name="register")
]