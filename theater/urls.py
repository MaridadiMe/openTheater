from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/', views.CategoryList.as_view()),
    path('languages/', views.LanguageList.as_view())
]