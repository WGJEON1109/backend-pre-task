from django.urls import path
from api.front import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.index, name="index"),
    path("detail", views.detail_profile, name="detail"),
    path("create", views.create, name="create"),
    path("login", auth_view.LoginView.as_view(), name="login"),
]
