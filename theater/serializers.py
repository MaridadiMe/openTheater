from rest_framework import serializers
from . models import Category, Language


class CategorySerializer(serializers.ModelSerializer):
    

    class Meta:
        model =  Category
        # fields = "__all__"
        fields = ('name', 'description', 'uuid')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('uuid','name')