"""
URL configuration for study_groups project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

from core import views

router = routers.DefaultRouter()
router.register(r'api/categories', views.CategoryViewSet)
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/comments', views.CommentViewSet)

urlpatterns = [
	path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/users/register/', RegisterView.as_view(), name='rest_register'),
    path('api/users/login/', LoginView.as_view(), name='rest_login'),
    path('api/users/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/users/user/', UserDetailsView.as_view(), name='rest_user_details'),
]
