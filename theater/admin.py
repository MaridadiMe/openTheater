from django.contrib import admin

from . models import Category, Language, Movie, Movie_category, Actor, Movie_actor

# Register your models here.
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Movie)
admin.site.register(Movie_category)
admin.site.register(Actor)
admin.site.register(Movie_actor)
