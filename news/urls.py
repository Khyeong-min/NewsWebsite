from django.contrib import admin
from django.urls import path
from .views import CategoryKeyword, HeadLine
from django.conf.urls.static import static


urlpatterns = [
    path('Category&Keyword/', CategoryKeyword.as_view()),
    path('HeadLine/', HeadLine.as_view())
]