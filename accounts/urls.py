from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    SignupView,
    LogoutView,
    UserListCreateView,
    UserDetailView,
    UserQuizHistoryView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<str:username>/', UserDetailView.as_view(), name='user-detail'),
    path('<str:username>/history/', UserQuizHistoryView.as_view(), name='user-detail'),
]
