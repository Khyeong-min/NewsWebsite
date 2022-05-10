from uuid import uuid4
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from .models import News
from comment.models import Comment
from LikeDislike.models import LikeDislike
from NewsWeb.settings import MEDIA_ROOT


class CategoryKeyword(APIView):
    def get(self, request):
        """
        키워드 정렬 최신기사 10개 정렬
        """
        news_element_list = News.objects.all().order_by('-id')


        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/Login.html")

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/Login.html")

        return render(request, "NewsWeb/Category&Keyword.html",
                      context=dict(news_element_list=news_element_list,
                                   user=user))


class HeadLine(APIView):
    def get(self, request):
        """
        키워드에 맞는 뉴스기사들의 헤드라인만 정렬
        """
        news_element_list = News.objects.all().order_by('-id')
        LnD_element_list = LikeDislike.objects.all().order_by('-id')


        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/Login.html")

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/Login.html")

        return render(request, "NewsWeb/HeadLine.html", context=dict(news_element_list=news_element_list,
                                                                     LnD_element_list=LnD_element_list,
                                                                     user=user))


class NewsComment(APIView):
    def get(self, request):
        """
        idNews에 맞는 신문의 모든 요소들을 출력하는 기능
        """
        news_element_list = News.objects.all().order_by('-id')
        comment_element_list = Comment.objects.all().order_by('-id')
        LnD_element_list = LikeDislike.objects.all().order_by('-id')

        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/Login.html")

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/Login.html")

        return render(request, "NewsWeb/News&Comment.html", context=dict(news_element_list=news_element_list,
                                                                         comment_element_list=comment_element_list,
                                                                         LnD_element_list=LnD_element_list,
                                                                         user=user))


