from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import date


def home_page(request):
    today = date.today()
    context = {'current_date': today}
    response = render(request, 'home.html', context)
    return HttpResponse(response)


def root(request):
    response = render(request, 'home.html')
    return HttpResponse(response)  
