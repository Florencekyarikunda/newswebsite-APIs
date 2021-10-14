from django.shortcuts import render
# import requests
from newspage.models import Articles
API_KEY="56082198622f4891923b76a2fda0c2e8"

def home(request):
 country = request.GET.get('country')
 category = request.GET.get('category')

 if country:
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    response = requests.json()
    data = response.json()
    articles = data['articles']
 else:
     url=f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
     response = requests.get(url)
     data = response.json()
     articles = data['articles']