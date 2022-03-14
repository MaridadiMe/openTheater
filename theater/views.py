from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # returns the index page which bootstaps angular app
    # front end is a single page app created in angular
    return render(request, 'theater/index.html')
