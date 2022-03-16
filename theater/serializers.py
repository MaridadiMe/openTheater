from rest_framework import serializers
from . models import Category, Language


class CategorySerializer(serializers.ModelSerializer):
    

    class Meta:
        model =  Category
        fields = "__all__"
        # fields = ('id','name', 'description', 'creator')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id','name')