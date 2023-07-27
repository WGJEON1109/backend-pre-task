from rest_framework import generics, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from apps.account.models import CustomUser
from api.account.serializers import CustomUserSerializer
import logging

logger = logging.getLogger("api")


class GetUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        logger.info("GetAllUsersView: [GET] 요청")
        return super().get(request, *args, **kwargs)


class GetUserView(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        logger.info("GetUserView: [GET] 요청")
        return super().get(request, *args, **kwargs)

    # 유저 삭제
    def delete(self, request, *args, **kwargs):
        logger.info("DeleteUserView: [DELETE] 요청")
        return super().delete(request, *args, **kwargs)


class RegisterView(generics.GenericAPIView):
    def post(self, request):
        logger.info("RegisterView: [POST] 회원가입 요청")
        logger.info(request.data)
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            result = Response(
                {
                    "user": serializer.data,
                    "message": "회원가입 성공",
                },
                status=status.HTTP_200_OK,
            )

            logger.info("회원가입 성공")
            return result
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginLogoutView(generics.GenericAPIView):
    def post(self, request):
        # 유저 확인
        email = request.data.get("email")
        password = request.data.get("password")
        logger.info(email)
        logger.info(password)
        logger.info("RegisterView: [POST] 로그인 요청")
        user = authenticate(email=email, password=password)
        logger.info(user)
        # 유저가 존재하는 경우
        if user is not None:
            serializer = CustomUserSerializer(user)

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            result = Response(
                {
                    "user": serializer.data,
                    "message": "로그인 성공",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )

            result.set_cookie("access", access_token, httponly=True)
            result.set_cookie("refresh", refresh_token, httponly=True)
            logger.info("로그인 성공")
            return result
        else:
            logger.error("user is None")
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # 로그아웃
    def delete(self, request):
        response = Response({"message": "로그아웃 성공"}, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
