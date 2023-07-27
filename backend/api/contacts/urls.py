from django.urls import path
from api.contacts import views

urlpatterns = [
    path("profiles", views.ProfileListCreateView.as_view(), name="profile-list-create"),
    path("profiles/<int:pk>", views.ProfileUpdateDestroyView.as_view(), name="profile-update"),
    path("labels", views.LabelCreateView.as_view(), name="labels-create"),
    path("labels/<int:pk>", views.LabelUpdateDestroyView.as_view(), name="labels-delete"),
    path(
        "profiles/remove_label",
        views.ProfileLabelDestroyView.as_view(),
        name="프로필-라벨 삭제",
    ),
]
