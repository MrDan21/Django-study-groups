from core.models import Category
<<<<<<< Updated upstream
from rest_framework import permissions, viewsets

from core.serializers import CategorySerializer
=======
from rest_framework import permissions, viewsets, generics, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from core.serializers import CategorySerializer
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from core.permissions import IsOwnerOrReadOnly
>>>>>>> Stashed changes
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
<<<<<<< Updated upstream
    permission_classes = [permissions.IsAuthenticated]
=======
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    http_method_names = ['get', 'post']

>>>>>>> Stashed changes

