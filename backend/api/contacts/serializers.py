from rest_framework import serializers
from apps.contacts.models import Label, Profile, ProfileLabel
import logging

logger = logging.getLogger("api")


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"

    # def validate_name(self, name):
    #     if Label.objects.filter(name=name).exists():
    #         raise serializers.ValidationError("이미 존재하는 Label입니다.")
    #     return name


class ProfileSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True)

    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        user = self.context.get("user_id")
        logger.info(user)
        validated_data["user_id"] = user
        logger.info(validated_data)

        labels_data = validated_data.pop("labels", [])
        profile = Profile.objects.create(**validated_data)
        if labels_data:
            for label_data in labels_data:
                try:  # 라벨 확인
                    label = Label.objects.get(name=label_data["name"])
                except Exception as e:  # 없으면 생성
                    print(e)
                    label = Label.objects.create(**label_data)
                try:  # profile: label 중복확인
                    ProfileLabel.objects.get(profile=profile, label=label)
                except Exception as e:  # 없으면 등록
                    print(e)
                    ProfileLabel.objects.create(profile=profile, label=label)
                profile.labels.add(label)

        return profile

    def update(self, instance, validated_data):
        instance.photo_url = validated_data.get("photo_url", instance.photo_url)
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.company = validated_data.get("company", instance.company)
        instance.position = validated_data.get("position", instance.position)
        instance.memo = validated_data.get("memo", instance.memo)
        instance.address = validated_data.get("address", instance.address)
        instance.birthday = validated_data.get("birthday", instance.birthday)
        instance.website = validated_data.get("website", instance.website)

        labels_data = validated_data.pop("labels", [])
        instance.labels.clear()
        for label_data in labels_data:
            try:
                label = Label.objects.get(name=label_data["name"])
            except:
                label = Label.objects.create(**label_data)
            instance.labels.add(label)
        instance.save()
        return instance
