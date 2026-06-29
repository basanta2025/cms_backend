from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import VendorFinancialDetail
from ..serializers import (
    VendorFinancialDetailCreateSerializer,
    VendorFinancialDetailListSerializer,
    VendorFinancialDetailRetrieveSerializer,
    VendorFinancialDetailUpdateSerializer,
)


class VendorFinancialDetailListView(CustomGenericListView):
    queryset = VendorFinancialDetail.objects.all()
    serializer_class = VendorFinancialDetailListSerializer
    success_response_message = "Vendor Financial Detail List Fetched Successfully"


class VendorFinancialDetailCreateView(CustomGenericCreateView):
    queryset = VendorFinancialDetail.objects.all()
    serializer_class = VendorFinancialDetailCreateSerializer
    success_response_message = "Vendor Financial Detail Created Successfully"


class VendorFinancialDetailUpdateView(CustomGenericUpdateView):
    queryset = VendorFinancialDetail.objects.all()
    serializer_class = VendorFinancialDetailUpdateSerializer
    success_response_message = "Vendor Financial Detail Updated Successfully"


class VendorFinancialDetailRetrieveView(CustomGenericRetrieveView):
    queryset = VendorFinancialDetail.objects.all()
    serializer_class = VendorFinancialDetailRetrieveSerializer
    success_response_message = "Vendor Financial Detail Retrieved Successfully"
