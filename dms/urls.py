"""
URL configuration for dms project.

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

# Include allows me to add new routes to the default router
from django.urls import path, include

# Allows routing client-sent API requests to views and methods
from rest_framework import routers

from dmsapp.views.user import UserViewSet

# Assigns router with DefaultRouter, removing the need to use "/" after a given endpoint
router = routers.DefaultRouter(trailing_slash=False)

# A list of specific paths that include methods as view sets and registered routes
urlpatterns = [
    # An empty string that will be reassigned to a new endpoint given by the request URL
    path("", include(router.urls)),

    # This path will lead a request body to my register user method to create a new user object
    path("register", UserViewSet.as_view({"post": "register_user"}), name="register"),
    path("login", UserViewSet.as_view({"post": "login_user"}, name="login")),

    # This path leads to the site administration interface
    path('admin/', admin.site.urls),
]
