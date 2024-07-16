from rest_framework import serializers
from core.models import Category, User, Group, Comment
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext as _

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'description', 'category', 'user_limit', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['description', 'user', 'group', 'created_at', 'updated_at']