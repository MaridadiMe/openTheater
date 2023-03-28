from django.db import models
import uuid
from django.contrib.auth.models import User
import os

# Create your models here.



class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    creator = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    date_created = models.DateTimeField('date created')
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'{self.first_name}, {self.second_name}'

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    creator = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

def movie_upload_path(instance, filename):
    return os.path.join(instance.title, filename)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.DateTimeField('date released')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=300)
    creator = models.ForeignKey(
        'auth.User',
        on_delete =  models.CASCADE
    )
    size = models.CharField(max_length=7)
    date_created = models.DateTimeField('date created')
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    actors = models.ManyToManyField(Actor, through='Movie_actor')
    categories = models.ManyToManyField(Category, through='Movie_category')
    downloads = models.ManyToManyField(User, through='Downloads', related_name='+')
    upload = models.FileField(upload_to=movie_upload_path)
    cover = models.FileField(upload_to=movie_upload_path)

    

    def __str__(self):
        return f'{self.title}, ({self.release_year})' 

class Movie_actor(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    actor_character = models.CharField(max_length=50)
    date_created = models.DateTimeField('date created')
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.actor_character



class Movie_category(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_created = models.DateTimeField('date created')
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)


class Language(models.Model):
    name = models.CharField(max_length = 50)
    creator = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    date_created = models.DateTimeField('date created')
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name
    

class Downloads(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='+')
    downloader = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField('date created')
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
