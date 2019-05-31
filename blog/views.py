from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import date
from blog.models import Article


def home_page(request):
    current_date = date.today()
    article = Article.objects.filter(draft=False).order_by('-published_date')
    context = {'date': current_date, 'article': article}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def root(request):
    return HttpResponseRedirect('home/')


def articles_page(request, id):
    articles = Article.objects.get(pk=id)
    context = {'title': 'DJANGO Article', 'articles': articles}
    response = render(request, 'articles_page.html', context)
    return HttpResponse(response)
  