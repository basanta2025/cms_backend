from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import VendorPaymentTerm
from ..serializers import (
    VendorPaymentTermCreateSerializer,
    VendorPaymentTermListSerializer,
    VendorPaymentTermRetrieveSerializer,
    VendorPaymentTermUpdateSerializer,
)


class VendorPaymentTermListView(CustomGenericListView):
    queryset = VendorPaymentTerm.objects.all()
    serializer_class = VendorPaymentTermListSerializer
    success_response_message = "Vendor Payment Term List Fetched Successfully"


class VendorPaymentTermCreateView(CustomGenericCreateView):
    queryset = VendorPaymentTerm.objects.all()
    serializer_class = VendorPaymentTermCreateSerializer
    success_response_message = "Vendor Payment Term Created Successfully"


class VendorPaymentTermUpdateView(CustomGenericUpdateView):
    queryset = VendorPaymentTerm.objects.all()
    serializer_class = VendorPaymentTermUpdateSerializer
    success_response_message = "Vendor Payment Term Updated Successfully"


class VendorPaymentTermRetrieveView(CustomGenericRetrieveView):
    queryset = VendorPaymentTerm.objects.all()
    serializer_class = VendorPaymentTermRetrieveSerializer
    success_response_message = "Vendor Payment Term Retrieved Successfully"
