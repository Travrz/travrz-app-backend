from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    UserChangePasswordView,
    SendPasswordResetEmailView,
    UserPasswordResetView,
)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", UserProfileView.as_view(), name="profile"),  # get, put, patch
    path("changepassword/", UserChangePasswordView.as_view(), name="changepassword"),
    path(
        "send-reset-password-email/",
        SendPasswordResetEmailView.as_view(),
        name="send-reset-password-email",
    ),
    path(
        "reset-password/<uid>/<token>/",
        UserPasswordResetView.as_view(),
        name="reset-password",
    ),
]
