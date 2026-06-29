from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import VendorBankAccount
from ..serializers import (
    VendorBankAccountCreateSerializer,
    VendorBankAccountListSerializer,
    VendorBankAccountRetrieveSerializer,
    VendorBankAccountUpdateSerializer,
)


class VendorBankAccountListView(CustomGenericListView):
    queryset = VendorBankAccount.objects.all()
    serializer_class = VendorBankAccountListSerializer
    success_response_message = "Vendor Bank Account List Fetched Successfully"


class VendorBankAccountCreateView(CustomGenericCreateView):
    queryset = VendorBankAccount.objects.all()
    serializer_class = VendorBankAccountCreateSerializer
    success_response_message = "Vendor Bank Account Created Successfully"


class VendorBankAccountUpdateView(CustomGenericUpdateView):
    queryset = VendorBankAccount.objects.all()
    serializer_class = VendorBankAccountUpdateSerializer
    success_response_message = "Vendor Bank Account Updated Successfully"


class VendorBankAccountRetrieveView(CustomGenericRetrieveView):
    queryset = VendorBankAccount.objects.all()
    serializer_class = VendorBankAccountRetrieveSerializer
    success_response_message = "Vendor Bank Account Retrieved Successfully"
