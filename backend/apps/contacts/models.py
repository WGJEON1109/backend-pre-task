from django.db import models
from apps.account.models import CustomUser


class Label(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = "label"


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    photo_url = models.URLField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)

    labels = models.ManyToManyField(Label, through="ProfileLabel")
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="profile", null=True
    )

    class Meta:
        managed = True
        db_table = "profile"


class ProfileLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "profile_label"
        unique_together = (("profile", "label"),)

    def __str__(self):
        return f"{self.profile.name} - {self.label.name}"
