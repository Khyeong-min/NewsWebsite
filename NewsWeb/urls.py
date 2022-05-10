"""NewsWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import Sub
from user.views import LogIn
from news.views import CategoryKeyword, HeadLine, NewsComment
from django.conf import settings
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('', LogIn.as_view()),
    path('Category&Keyword/', CategoryKeyword.as_view()),
    path('HeadLine/', HeadLine.as_view()),
    path('News&Comment/', NewsComment.as_view()),
    path('user/', include('user.urls'))
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)