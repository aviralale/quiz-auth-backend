from django.urls import path
from .views import (
    UserListCreateView,
    UserDetailView,
    CustomAuthToken,
    SignupView,
    LogoutView,
)

urlpatterns = [
    path("login/", CustomAuthToken.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", UserListCreateView.as_view(), name="user-list-create"),
    path("<str:username>", UserDetailView.as_view(), name="user-detail"),
]
