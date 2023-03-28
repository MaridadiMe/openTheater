from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('openTheater/categories/', views.CategoryList.as_view()),
    path('openTheater/languages/', views.LanguageList.as_view()),
    path('openTheater/get-movie-list-to-watch/', views.MovieWatchList.as_view()),
    path('openTheater/get-movie-to-watch-details/<str:uuid>', views.MovieDetails.as_view()),
]