from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient



# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='17af1b67e52a44fa85a60b1f052df07d')
    headLines = newsapi.get_top_headlines(sources='ign, cnn')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, "main/index.html", context={"mylist": mylist})
