from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .renderers import UserRenderer
from .serializers import (
    UserSerializer,
    UserLoginSerializer,
    UserChangePasswordSerializer,
    SendPasswordResetEmailSerializer,
    UserPasswordResetSerializer,
)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserRegistrationView(generics.CreateAPIView):
    """Create a new user in the system"""

    renderer_classes = [UserRenderer]
    serializer_class = UserSerializer


# auth token and refresh token
class UserLoginView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = UserLoginSerializer
    renderer_classes = [UserRenderer]


class UserProfileView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    renderer_classes = [UserRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"msg": "Password Changed Successfully"}, status=status.HTTP_200_OK
        )


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"msg": "Password Reset link send. Please check your Email"},
            status=status.HTTP_200_OK,
        )


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"msg": "Password Reset Successfully"}, status=status.HTTP_200_OK
        )
