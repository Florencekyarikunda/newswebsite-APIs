# from requests.api import request,reverse
# from news import newspage, User
# from requests import get_sources, get_articles
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.forms import CustomUserCreationForm



# API_KEY="56082198622f4891923b76a2fda0c2e8"


# def loginUser(request):
#     page = 'login'
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)
  
#     if user is not None:
#          login(request,user)
#          return redirect('newspage')
#     return render(request,"newspage/login_register.html", {'page':page})


# def logoutUser(request):
#     logout(request)
#     return redirect('login')

# def registerUser(request):
#     page = 'register'
#     form = CustomUserCreationForm()
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()

#         # if user is not None:
#         #     if user is not None:
#         #         login(request, user)
#         #         return redirect('page')

#     context = {'form': form, 'page': page}
#     return render(request, 'newspage/login_register.html', context)

# @login_required(login_url='login')
# def home(request):
#     sources = get_sources('business')
#     sports_sources = get_sources('sports')
#     technology_sources = get_sources('technology')
#     entertainment_sources = get_sources('entertainment')
#     corona_sources = get_sources('corona')
#     title = "News Desk"
#     return render(request, 'newspage/index.html' ,{"title":title, "sources":sources, "sports_sources":sports_sources, "technology_sources":technology_sources, "entertainment_sources":entertainment_sources, "corona_sources":corona_sources})


# def articles(request):
#     '''
#     view articles page
#     '''
#     articles = get_articles(id)
#     title = f'NH | {id}'

#     return render(request,'newspage/articles.html', {"title":title, "articles":articles})

   