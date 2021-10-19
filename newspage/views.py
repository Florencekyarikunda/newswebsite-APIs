from django.shortcuts import render
import requests 

API_KEY="56082198622f4891923b76a2fda0c2e8"

def home(request):
 
   return render(request,'newspage/index.html')

def article(request):
   country = request.GET.get('country')
   category = request.GET.get('category')

   if country:
         url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
         response = requests.json()
         data = response.json()
         articles = data['articles']
   else:
      url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
      response = requests.get(url)
      data = response.json()
      articles = data['articles']


   context = {
         'articles' : articles
      }
   return render(request, 'newspage/articles.html', context)
 
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


