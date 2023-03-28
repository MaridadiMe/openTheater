from rest_framework import serializers
from . models import Category, Language, Movie,Actor, Movie_actor
from django.contrib.auth.models import User



class CategorySerializer(serializers.ModelSerializer):   
    class Meta:
        model =  Category
        # fields = "__all__"
        fields = ('name', 'description', 'uuid')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('uuid','name')

class MovieActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_actor
        fields = ['movie', 'actor','actor_character']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('first_name', 'second_name')

class MovieWatchListSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('title', 'release_year','actors','cover', 'uuid')

class MovieDetailsSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('title', 'description','release_year','actors','cover', 'upload', 'uuid')