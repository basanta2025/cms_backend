from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import CustomUser
from ..serializers import (
    CustomUserCreateSerializer,
    CustomUserRetrieveSerializer,
    CustomUserUpdateSerializer,
    UserListSerializer,
)

User = get_user_model()


class UserCreateView(CustomGenericCreateView):
    serializer_class = CustomUserCreateSerializer
    queryset = User.objects.all()


class UserUpdateView(CustomGenericUpdateView):
    serializer_class = CustomUserUpdateSerializer
    queryset = User.objects.all()
    success_response_message = "User updated successfully."


class UserRetrieveView(CustomGenericRetrieveView):
    serializer_class = CustomUserRetrieveSerializer
    queryset = User.objects.all()
    success_response_message = "Users retrieved successfully."


class UserListView(CustomGenericListView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer
    success_response_message = "Users fetched successfully."
    # filterset_class = UserFilters
    search_fields = [
        "username",
        "email",
        "mobile_no",
        "palika",
        "tole",
    ]


# class ChangeUserPasswordView(CustomGenericUpdateView):
#     serializer_class = ChangePasswordSerializer
#     success_response_message = "Password changed successfully."
#     queryset = User.objects.all()

#     permission_classes = [
#         IsAuthenticated,
#     ]

#     def get_object(self):
#         user = self.request.user
#         self.kwargs["user"] = user
#         return user


# class UpdateUserPasswordView(CustomGenericUpdateView):
#     serializer_class = ChangePasswordSerializer
#     queryset = User.objects.all()
#     success_response_message = "Password updated successfully."
#     permission_classes = [
#         IsAuthenticated,
#     ]

#     def get_object(self):
#         kwargs = self.kwargs
#         user_id = kwargs["pk"]
#         user = CustomUser.objects.filter(id=user_id).first()
#         if not user:
#             message = "User not found."
#             return CustomAPIResponse.custom_error_response(message=message)
#         kwargs["user"] = user
#         return user


class UserDeleteView(APIView):
    permission_classes = []
    # serializer_class = UserDeleteSerializer
    queryset = CustomUser.objects.all()

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        user = CustomUser.objects.filter(id=user_id).first()
        if not user:
            return Response(
                {"message": "User not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.is_active = False
        user.save()

        # serializer = self.serializer_class(user)
        return Response(
            {"message": "User deleted successfully.", "data": None},
            status=status.HTTP_200_OK,
        )
