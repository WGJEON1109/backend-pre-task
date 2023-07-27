from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.contacts.models import Profile, Label, ProfileLabel
from api.contacts import serializers
import logging

logger = logging.getLogger("api")


# profile 조회, 생성
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        logger.info("ProfileListCreateView: [GET] 요청")
        queryset = self.filter_queryset(self.get_queryset())
        logger.info("API 호출한 user 데이터 read")
        queryset = queryset.filter(user_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        logger.info("ProfileListCreateView: [POST] 요청")

        serializer = self.get_serializer(
            data=request.data, context={"user_id": request.user.id}
        )  # context로 유저 식별정보 전달
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# profile 조회, 업데이트, 삭제
class ProfileUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def get(self, request, *args, **kwargs):
        logger.info("ProfileUpdateDestroyView: [GET] 요청")
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        logger.info("ProfileUpdateDestroyView: [PUT] 요청")
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        logger.info("ProfileUpdateDestroyView: [DELETE] 요청")
        return super().delete(request, *args, **kwargs)


# label 생성
# 구글: label 생성 > profile 생성
# label 먼저 생성 후 > label을 profile 생성 API에 같이 보내면 many-to-many하는 방향으로
class LabelCreateView(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = serializers.LabelSerializer

    # 라벨 전체 목록 조회
    def get(self, request, *args, **kwargs):
        logger.info("ProfileUpdateDestroyView: [GET] 요청")
        return super().get(request, *args, **kwargs)

    # 라벨 생성
    def post(self, request, *args, **kwargs):
        logger.info("ProfileUpdateDestroyView: [POST] 요청")
        return super().post(request, *args, **kwargs)


class LabelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = serializers.LabelSerializer

    # 라벨 1개 조회
    def get(self, request, *args, **kwargs):
        logger.info("ProfileUpdateDestroyView: [GET] 요청")

        return super().get(request, *args, **kwargs)

    # 라벨 삭제
    def delete(self, request, *args, **kwargs):
        logger.info("ProfileUpdateDestroyView: [DELETE] 요청")

        return super().delete(request, *args, **kwargs)


# 프로필-라벨 매핑 삭제
class ProfileLabelDestroyView(generics.GenericAPIView):
    queryset = ProfileLabel.objects.all()

    def post(self, request):
        logger.info("ProfileUpdateDestroyView: [POST] 요청")
        logger.info("프로필에서 라벨 제거 요청")
        profile_id = request.data.get("profile_id")
        label_id = request.data.get("label_id")

        profile = Profile.objects.get(id=profile_id)
        label = Label.objects.get(id=label_id)
        ProfileLabel.objects.filter(profile=profile, label=label).delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
