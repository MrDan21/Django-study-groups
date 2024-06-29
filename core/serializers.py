from rest_framework import serializers
from core.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'created_at', 'updated_at']