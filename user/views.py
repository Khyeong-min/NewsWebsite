from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response


# Create your views here.
class SignUP(APIView):
    def get(self, request):
        return render(request, "user/Signup.html")

    def post(self, request):
        # 회원가입
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        nickname = request.data.get('nickname', None)
        user_id = request.data.get('user_id', None)

        User.objects.create(
            email=email,
            nickname=nickname,
            password=make_password(password),
            user_id=user_id
        )

        return Response(status=200)


class LogIn(APIView):
    def get(self, request):
        return render(request, "user/Login.html")

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        # 회원정보 동일한지 비교
        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))

        if user.check_password(password):

            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))
