from django.urls import include, path

from .views import (
    ChangePasswordView,
    LoginView,
    LogoutView,
    PermissionsCategoryListView,
    PermissionsListDropdownView,
    PermissionsListView,
    RefreshTokenView,
    RolesCreateView,
    RolesListDropdownView,
    RolesListView,
    RolesRetrieveView,
    RolesUpdateView,
    UserCreateView,
    UserDeleteView,
    UserListView,
    UserRetrieveView,
    UserSignUpAPIView,
    UserUpdateView,
)

auth_patterns = [
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("refresh-token", RefreshTokenView.as_view(), name="refresh_token"),
    path("change-password", ChangePasswordView.as_view(), name="change_password"),
    path("signup", UserSignUpAPIView.as_view(), name="signup"),
]
user_patterns = [
    path("list", UserListView.as_view(), name="user-list"),
    path("create", UserCreateView.as_view(), name="user-create"),
    path("<int:pk>", UserRetrieveView.as_view(), name="user-retrieve"),
    path("<int:pk>/update", UserUpdateView.as_view(), name="user-update"),
    # path("<int:pk>/delete", UserDeleteView.as_view(), name="user-delete"),
]
permissions_patterns = [
    path(
        "categories/list",
        PermissionsCategoryListView.as_view(),
        name="permissions-category-list",
    ),
    path("list", PermissionsListView.as_view(), name="permissions-list"),
    path(
        "dropdown",
        PermissionsListDropdownView.as_view(),
        name="permissions-list-dropdown",
    ),
]
roles_patterns = [
    path("list", RolesListView.as_view(), name="roles-list"),
    path("dropdown", RolesListDropdownView.as_view(), name="roles-list-dropdown"),
    path("create", RolesCreateView.as_view(), name="roles-create"),
    path("<int:pk>", RolesRetrieveView.as_view(), name="roles-retrieve"),
    path("<int:pk>/update", RolesUpdateView.as_view(), name="roles-update"),
]

urlpatterns = [
    path("auth/", include((auth_patterns, "authentication"), namespace="auth")),
    path("users/", include((user_patterns, "users"), namespace="users")),
    path(
        "permissions/",
        include((permissions_patterns, "permissions"), namespace="permissions"),
    ),
    path("roles/", include((roles_patterns, "roles"), namespace="roles")),
]
