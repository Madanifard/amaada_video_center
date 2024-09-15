
from rest_framework import serializers
from .models import Category, Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'file', 'size', 'uploaded_at']


class CategorySerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'videos']
