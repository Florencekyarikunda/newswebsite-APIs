from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

from news.App_Login.forms import CreateNewUser
from news.App_Login.models import UserProfile

# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method =='POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
    return render(request, 'App_Login/signup.html', context={'title':'Sign up.social','form':form})

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Login:home'))
    return render(request, 'App_Login/login.html', context={'title':'Login', 'form':form})