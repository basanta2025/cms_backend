from apps.authentication.permissions.permissions import (
    CustomAuthenticationPermission,
    CustomIsAuthenticatedPermission,
    # PermissionLists,
)
from base.views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..filters import BaseUnitFilter
from ..models import BaseUnit
from ..serializers import (
    BaseUnitCreateSerializer,
    BaseUnitDropdownSerializer,
    BaseUnitForConversionView,
    BaseUnitSerializer,
    BaseUnitUpdateSerializer,
)


class BaseUnitListView(CustomGenericListView):
    queryset = BaseUnit.objects.all()
    serializer_class = BaseUnitSerializer
    success_response_message = "Base Unit fetched successfully."
    search_fields = ["name"]
    filterset_class = BaseUnitFilter

    # def get_permissions(self):
    #     return [
    #         CustomAuthenticationPermission(
    #             models={
    #                 PermissionLists.HTTP_GET_METHOD: PermissionLists.BASEUNIT,
    #             },
    #         )
    #     ]


class BaseUnitDropdownListView(CustomGenericListView):
    queryset = BaseUnit.objects.filter(is_active=True).only("name", "id", "parent")
    serializer_class = BaseUnitDropdownSerializer
    search_fields = ["name"]

    def get_permissions(self):
        return [CustomIsAuthenticatedPermission()]


class BaseUnitRetrieveView(CustomGenericRetrieveView):
    queryset = BaseUnit.objects.all()
    serializer_class = BaseUnitSerializer
    search_fields = ["name"]
    success_response_message = "Base Unit retrieved successfully."

    # def get_permissions(self):
    #     return [
    #         CustomAuthenticationPermission(
    #             models={
    #                 PermissionLists.HTTP_GET_METHOD: PermissionLists.BASEUNIT,
    #             },
    #         )
    #     ]


class BaseUnitCreateView(CustomGenericCreateView):
    queryset = BaseUnit.objects.all()
    serializer_class = BaseUnitCreateSerializer
    search_fields = ["name"]
    success_response_message = "Base Unit created successfully."

    # def get_permissions(self):
    #     return [
    #         CustomAuthenticationPermission(
    #             models={
    #                 PermissionLists.HTTP_POST_METHOD: PermissionLists.BASEUNIT,
    #             },
    #         )
    #     ]


class BaseUnitUpdateView(CustomGenericUpdateView):
    queryset = BaseUnit.objects.all()
    serializer_class = BaseUnitUpdateSerializer
    search_fields = ["name"]
    success_response_message = "Base Unit updated successfully."

    # def get_permissions(self):
    #     return [
    #         CustomAuthenticationPermission(
    #             models={
    #                 PermissionLists.HTTP_PATCH_METHOD: PermissionLists.BASEUNIT,
    #             },
    #         )
    #     ]
