from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView

from base.views.generic_views import (
    CustomAPIResponse,
    CustomGenericCreateView,
    CustomGenericUpdateView,
)

from ..models import CustomUser
from ..permissions.permissions import (
    IsAuthenticated,
)
from ..serializers import (
    ChangePasswordSerializer,
    LoginSerializer,
    LogoutSerializer,
    UserSignUpSerializer,
)

User = get_user_model()


class UserSignUpAPIView(CustomGenericCreateView):
    serializer_class = UserSignUpSerializer
    permission_classes = []

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if not serializer.is_valid():
            errors = serializer.errors
            message = self._get_message(data=errors)
            if message:
                return CustomAPIResponse.custom_error_response(message=message)
        serializer.save()
        # response = user.tokens(request)
        return CustomAPIResponse.custom_success_response(
            data=serializer.data,
            message="Signup successful",
        )


class RefreshTokenView(TokenRefreshView):
    permission_classes = []


class LoginView(GenericAPIView):
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        from datetime import datetime

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        meta_data = {
            "timestamp": now,
        }
        if serializer.is_valid():
            return Response(
                {
                    "success": True,
                    "message": "Logged in successfully.",
                    "meta_data": meta_data,
                    **serializer.validated_data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "message": "Invalid Credentials.",
                "meta_data": meta_data,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class ChangePasswordView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ChangePasswordSerializer
    http_method_names = ["patch"]

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {"message": "Logged out successfully."}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "Logout failed.", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
