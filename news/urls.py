from django.contrib import admin
from django.urls import path
from .views import CategoryKeyword, HeadLine, NewsComment
from django.conf.urls.static import static


urlpatterns = [
    path('Category&Keyword/', CategoryKeyword.as_view()),
    path('HeadLine/', HeadLine.as_view()),
    path('News&Comment/', NewsComment.as_view())
]