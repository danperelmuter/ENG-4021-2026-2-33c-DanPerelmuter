"""
URL configuration for GradePuc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from GradeP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home2, name='home'),
    path('filmes/novo/', movie_create, name='movie_create'),
    path('filmes/<int:pk>/editar/', movie_update, name='movie_update'),
    path('filmes/<int:pk>/deletar/', movie_delete, name='movie_delete'),
]
