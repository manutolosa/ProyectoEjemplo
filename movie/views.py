from re import search
from django.shortcuts import render
from django.shortcuts import HttpResponse

import movie

from .models import Movie

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request,'home.html',{'searchTerm':searchTerm, 'movies':movies})

def about(request):
    return HttpResponse('Welcome to About page</h1>')