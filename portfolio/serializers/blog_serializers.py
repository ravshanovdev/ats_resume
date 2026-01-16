from rest_framework import serializers
from portfolio.models.blog import Blog



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'category', 'title', 'description', 'image', 'created_at']






