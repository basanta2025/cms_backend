from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import VendorContactPerson
from ..serializers import (
    VendorContactPersonCreateSerializer,
    VendorContactPersonListSerializer,
    VendorContactPersonRetrieveSerializer,
    VendorContactPersonUpdateSerializer,
)


class VendorContactPersonListView(CustomGenericListView):
    queryset = VendorContactPerson.objects.all()
    serializer_class = VendorContactPersonListSerializer
    success_response_message = "Vendor Contact Person List Fetched Successfully"


class VendorContactPersonCreateView(CustomGenericCreateView):
    queryset = VendorContactPerson.objects.all()
    serializer_class = VendorContactPersonCreateSerializer
    success_response_message = "Vendor Contact Person Created Successfully"


class VendorContactPersonUpdateView(CustomGenericUpdateView):
    queryset = VendorContactPerson.objects.all()
    serializer_class = VendorContactPersonUpdateSerializer
    success_response_message = "Vendor Contact Person Updated Successfully"


class VendorContactPersonRetrieveView(CustomGenericRetrieveView):
    queryset = VendorContactPerson.objects.all()
    serializer_class = VendorContactPersonRetrieveSerializer
    success_response_message = "Vendor Contact Person Retrieved Successfully"
