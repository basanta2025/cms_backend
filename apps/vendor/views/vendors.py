from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import Vendor
from ..serializers import (
    VendorCreateSerializer,
    VendorListSerializer,
    VendorRetrieveSerializer,
    VendorUpdateSerializer,
)


class VendorListView(CustomGenericListView):
    queryset = Vendor.objects.all()
    serializer_class = VendorListSerializer
    success_response_message = "Vendor List Fetched Successfully"


class VendorCreateView(CustomGenericCreateView):
    queryset = Vendor.objects.all()
    serializer_class = VendorCreateSerializer
    success_response_message = "Vendor Created Successfully"


class VendorUpdateView(CustomGenericUpdateView):
    queryset = Vendor.objects.all()
    serializer_class = VendorUpdateSerializer
    success_response_message = "Vendor Updated Successfully"


class VendorRetrieveView(CustomGenericRetrieveView):
    queryset = Vendor.objects.all()
    serializer_class = VendorRetrieveSerializer
    success_response_message = "Vendor Retrieved Successfully"
