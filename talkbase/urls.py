"""
URL configuration for talkbase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import permissions
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from authenticate.views import welcome
from djoser import views as djoser_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Talkbase API",
        default_version='v1',
        description="API documentation for Talkbase project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/users',  djoser_views.UserViewSet.as_view({"post": "create"}), name="user-registration"),
    path('auth/users/me', djoser_views.UserViewSet.as_view({"get": "me"}), name="user-me"),
    path('auth/jwt', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/jwt/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/jwt/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('', welcome, name='welcome'),
    path('posts/', include('post.urls')),
]
