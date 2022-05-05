from uuid import uuid4

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
import os
from NewsWeb.settings import MEDIA_ROOT

# Create your views here.
class Comment(APIView):
    def get(self, request):
        """
        기사 주소에 맞는 id를 가진 댓글을 출력하는 기능
        """
        pass