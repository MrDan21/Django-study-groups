from rest_framework import serializers
<<<<<<< Updated upstream
from core.models import Category
=======
from core.models import Category, User
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext as _

>>>>>>> Stashed changes

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'created_at', 'updated_at']