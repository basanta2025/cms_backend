from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import VendorDocument
from ..serializers import (
    VendorDocumentCreateSerializer,
    VendorDocumentListSerializer,
    VendorDocumentRetrieveSerializer,
    VendorDocumentUpdateSerializer,
)


class VendorDocumentListView(CustomGenericListView):
    queryset = VendorDocument.objects.all()
    serializer_class = VendorDocumentListSerializer
    success_response_message = "Vendor Document List Fetched Successfully"


class VendorDocumentCreateView(CustomGenericCreateView):
    queryset = VendorDocument.objects.all()
    serializer_class = VendorDocumentCreateSerializer
    success_response_message = "Vendor Document Created Successfully"


class VendorDocumentUpdateView(CustomGenericUpdateView):
    queryset = VendorDocument.objects.all()
    serializer_class = VendorDocumentUpdateSerializer
    success_response_message = "Vendor Document Updated Successfully"


class VendorDocumentRetrieveView(CustomGenericRetrieveView):
    queryset = VendorDocument.objects.all()
    serializer_class = VendorDocumentRetrieveSerializer
    success_response_message = "Vendor Document Retrieved Successfully"
