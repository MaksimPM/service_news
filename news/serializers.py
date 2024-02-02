from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
