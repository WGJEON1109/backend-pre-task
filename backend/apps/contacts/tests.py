from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.account.models import CustomUser
from apps.contacts.models import Profile, Label, ProfileLabel


class ProfileListCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="testuser@test.com", password="testpassword"
        )
        self.token = str(TokenObtainPairSerializer.get_token(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

    def test_get_profile_list(self):
        response = self.client.get("/api/profiles")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_profile(self):
        data = {
            "name": "Test Profile",
            "email": "test@example.com",
            "phone": "123-456-7890",
        }
        response = self.client.post("/api/profiles", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LabelCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="testuser@test.com", password="testpassword"
        )
        self.client.login(email="testuser@test.com", password="testpassword")

    def test_get_label_list(self):
        response = self.client.get("/api/labels")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_label(self):
        data = {
            "name": "Test Label",
        }
        response = self.client.post("/api/labels", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LabelUpdateDestroyViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="testuser@test.com", password="testpassword"
        )
        self.client.login(email="testuser@test.com", password="testpassword")
        self.label = Label.objects.create(name="Test Label")

    def test_get_label(self):
        response = self.client.get(f"/api/labels/{self.label.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_label(self):
        response = self.client.delete(f"/api/labels/{self.label.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProfileLabelDestroyViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="testuser@test.com", password="testpassword"
        )
        self.client.login(email="testuser@test.com", password="testpassword")
        self.profile = Profile.objects.create(
            name="Test Profile", email="test@example.com", phone="123-456-7890"
        )
        self.label = Label.objects.create(name="Test Label")
        self.profile_label = ProfileLabel.objects.create(profile=self.profile, label=self.label)

    def test_remove_label_from_profile(self):
        data = {
            "profile_id": self.profile.id,
            "label_id": self.label.id,
        }
        response = self.client.post("/api/profiles/remove-label/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
