from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import CategorySerializer, LanguageSerializer, MovieSerializer
from . models import Category, Language, Movie

# Create your views here.

def index(request):
    # returns the index page which bootstaps angular app
    # front end is a single page app created in angular
    return render(request, 'theater/index.html')


class  CategoryList(APIView):
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)        
        return JsonResponse(serializer.data, safe=False)
        

class LanguageList(APIView):
    def get(self, request):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return JsonResponse(serializer.data, safe=False)

class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)


