from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("갯으로 호출")
        return render(request,"NewsWeb/Category&Keyword.html")

    def post(self, request):
        print("포스트로 호출")
        return render(request, "NewsWeb/Category&Keyword.html")