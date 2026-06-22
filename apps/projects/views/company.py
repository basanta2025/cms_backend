from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import Company
from ..serializers import (
    CompanyCreateSerializer,
    CompanyListSerializer,
    CompanyRetrieveSerializer,
    CompanyUpdateSerializer,
)


class CompanyCreateView(CustomGenericCreateView):
    serializer_class = CompanyCreateSerializer
    queryset = Company.objects.all()
    success_response_message = "Company created successfully."


class CompanyListView(CustomGenericListView):
    serializer_class = CompanyListSerializer
    queryset = Company.objects.all()
    success_response_message = "Companies fetched successfully."


class CompanyRetrieveView(CustomGenericRetrieveView):
    serializer_class = CompanyRetrieveSerializer
    queryset = Company.objects.all()
    success_response_message = "Company retrieved successfully."


class CompanyUpdateView(CustomGenericUpdateView):
    serializer_class = CompanyUpdateSerializer
    queryset = Company.objects.all()
    success_response_message = "Company updated successfully."
