from django.contrib import admin
from django.urls import path
from .views import NB


urlpatterns = [
    path('Profile', NB.as_view())
]