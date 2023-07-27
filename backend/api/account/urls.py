from django.urls import path
from api.account import views

urlpatterns = [
    path("users", views.GetUsersView.as_view(), name="user list"),
    path("register", views.RegisterView.as_view(), name="회원가입"),
    path("auth", views.LoginLogoutView.as_view(), name="로그인/로그아웃"),
    path("users/<int:pk>", views.GetUserView.as_view(), name="get_user"),
]
