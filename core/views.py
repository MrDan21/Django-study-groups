from core.models import Category
from rest_framework import permissions, viewsets
from core.serializers import CategorySerializer
from rest_framework import permissions, viewsets, generics, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from core.serializers import CategorySerializer
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from core.permissions import IsOwnerOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    http_method_names = ['get', 'post']
