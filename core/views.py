from core.models import Category
from rest_framework import permissions, viewsets
from core.serializers import CategorySerializer, GroupSerializer, CommentSerializer
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

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
