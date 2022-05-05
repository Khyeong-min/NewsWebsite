from django.urls import path
from .views import SignUP, LogIn


urlpatterns = [
    path('Signup', SignUP.as_view()),
    path('Login', LogIn.as_view())
]
