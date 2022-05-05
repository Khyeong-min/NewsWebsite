from uuid import uuid4

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import User
import os
from NewsWeb.settings import MEDIA_ROOT


# Create your views here.
class CategoryKeyword(APIView):
    def get(self, request):
        # keyword_element_list = KeywordElement.objects.all().order_by('-id')
        # news_element_list = NewsElement.objects.all().order_by('-id')

        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/Login.html")

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/Login.html")

        return render(request, "NewsWeb/Category&Keyword.html")
    # context=dict(keyword_element_list=keyword_element_list,
    # news_element_list=news_element_list,
    # user=user))


class HeadLine(APIView):
    def get(self, request):
        """
        키워드에 맞는 뉴스기사들의 헤드라인만 정렬
        """
        # news_element_list = NewsElement.objects.all().order_by('-id')

        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/Login.html")

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/Login.html")

        return render(request, "NewsWeb/HeadLine.html")


        # context=dict(news_element_list=news_element_list, user=user)