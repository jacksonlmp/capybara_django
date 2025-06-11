"""
URL configuration for capybara_django project.

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
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

@api_view(['GET'])
def root(request):
    return Response({
        'message': 'Welcome to the Capybara Django API',
    })
    
urlpatterns = [
    # Django
    path('admin/', admin.site.urls),
    
    # Third-party apps
    path('api-auth/', include('rest_framework.urls')),
    
    # Local
    path('', root)
]
