from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    creator = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    date_created = models.DateTimeField('date created')

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    creator = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.DateTimeField('date released')
    language = models.IntegerField()
    description = models.CharField(max_length=200)
    creator = models.ForeignKey(
        'auth.User',
        on_delete =  models.CASCADE
    )
    size = models.CharField(max_length=7)
    date_created = models.DateTimeField('date created')
    actors = models.ManyToManyField(Actor, through='Movie_actor')
    categories = models.ManyToManyField(Category, through='Movie_category')
    downloads = models.ManyToManyField(User, through='Downloads', related_name='+')

class Movie_actor(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    actor_character = models.CharField(max_length=50)
    date_created = models.DateTimeField('date created')



class Movie_category(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_created = models.DateTimeField('date created')


class Language(models.Model):
    name = models.CharField(max_length = 50)
    creator = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    date_created = models.DateTimeField('date created')
    

class Downloads(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='+')
    downloader = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField('date created')
