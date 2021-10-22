from requests.api import request
# import newspage
from .requests import get_sources, get_articles
# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import requests 
from django.contrib.auth.decorators import login_required
# from .forms import CustomUserCreationForm



API_KEY="56082198622f4891923b76a2fda0c2e8"

# def loginUser(request):
#     newspage = 'login'
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)
  
#     if user is not None:
#          login(request,user)
#          return redirect('newspage')
#     return render(request,"newspage/login_register.html", {'newspage':newspage})
   
# def logoutUser(request):
#     logout(request)
#     return redirect('login')

# def registerUser(request):
#     newpage = 'register'
#     form = CustomUserCreationForm()
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()

#         if user is not None:
#             if user is not None:
#                 login(request, user)
#                 return redirect('newspage')

#     context = {'form': form, 'newspage': newspage}
#     return render(request, 'newspage/login_register.html', context)

# @login_required(login_url='login')
def home(request):
    sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    corona_sources = get_sources('corona')
    title = "News Desk"

    return render(request, 'newspage/index.html' ,{"title":title, "sources":sources, "sports_sources":sports_sources, "technology_sources":technology_sources, "entertainment_sources":entertainment_sources, "corona_sources":corona_sources})


def articles(request):
    '''
    view articles page
    '''
    articles = get_articles(id)
    title = f'NH | {id}'

    return render(request,'newspage/articles.html', {"title":title, "articles":articles})

   
# def sources(request):
#    country = request.GET.get('country')
#    category = request.GET.get('category')

#    if country:
#          url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
#          response = requests.json()
#          data = response.json()
#          articles = data['articles']
#    else:
#       url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
#       response = requests.get(url)
#       data = response.json()
#       articles = data['articles']


#    context = {
#          'articles' : articles
#       }
#    return render(request, 'newspage/articles.html', context)
 
# def index():
#     '''
#     view root page function that returns the index the page and its data
#     '''
#     sources = get_sources('business')
#     sports_sources = get_sources('sports')
#     technology_sources = get_sources('technology')
#     entertainment_sources = get_sources('entertainment')
#     corona_sources = get_sources('corona')
#     title = "News Desk"

#     return render('index.html', title=title, sources=sources, sports_sources=sports_sources, technology_sources=technology_sources, entertainment_sources=entertainment_sources, corona_sources=corona_sources)

# class Sources:
#     sources = get_sources('business')
#     sports_sources = get_sources('sports')
#     technology_sources = get_sources('technology')
#     entertainment_sources = get_sources('entertainment')
#     corona_sources = get_sources('corona')
#     title = "News Desk"
    
#     return render('index.html', title=title, sources=sources, sports_sources=sports_sources, technology_sources=technology_sources, entertainment_sources=entertainment_sources, corona_sources=corona_sources)


