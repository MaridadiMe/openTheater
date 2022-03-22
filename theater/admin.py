from django.contrib import admin

from . models import Category, Language, Movie

# Register your models here.
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Movie)
