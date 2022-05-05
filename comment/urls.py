from django.contrib import admin
from django.urls import path
from .views import Comment
from django.conf.urls.static import static

urlpatterns =[
    path('comment', Comment.as_view())
]