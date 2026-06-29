from base.serializers import BaseModelSerializer, ExcludeFields, serializers
from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import VendorLabourType
from ..serializers import (
    VendorLabourTypeCreateSerializer,
    VendorLabourTypeListSerializer,
    VendorLabourTypeRetrieveSerializer,
    VendorLabourTypeUpdateSerializer,
)


class VendorLabourTypeListView(CustomGenericListView):
    queryset = VendorLabourType.objects.all()
    serializer_class = VendorLabourTypeListSerializer
    success_response_message = "Vendor Labour Type List Fetched Successfully"


class VendorLabourTypeCreateView(CustomGenericCreateView):
    queryset = VendorLabourType.objects.all()
    serializer_class = VendorLabourTypeCreateSerializer
    success_response_message = "Vendor Labour Type Created Successfully"


class VendorLabourTypeUpdateView(CustomGenericUpdateView):
    queryset = VendorLabourType.objects.all()
    serializer_class = VendorLabourTypeUpdateSerializer
    success_response_message = "Vendor Labour Type Updated Successfully"


class VendorLabourTypeRetrieveView(CustomGenericRetrieveView):
    queryset = VendorLabourType.objects.all()
    serializer_class = VendorLabourTypeRetrieveSerializer
    success_response_message = "Vendor Labour Type Retrieved Successfully"
