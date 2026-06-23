from base.views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import MaterialCompany
from ..serializers import (
    MaterialCompanyCreateSerializer,
    MaterialCompanyListSerializer,
    MaterialCompanyRetrieveSerializer,
    MaterialCompanyUpdateSerializer,
)


class MaterialCompanyCreateView(CustomGenericCreateView):
    serializer_class = MaterialCompanyCreateSerializer
    queryset = MaterialCompany.objects.all()
    success_response_message = "Material Company created successfully."


class MaterialCompanyListView(CustomGenericListView):
    serializer_class = MaterialCompanyListSerializer
    queryset = MaterialCompany.objects.all()
    success_response_message = "Material Company fetched successfully."


class MaterialCompanyRetrieveView(CustomGenericRetrieveView):
    serializer_class = MaterialCompanyRetrieveSerializer
    queryset = MaterialCompany.objects.all()
    success_response_message = "Material Company retrieved successfully."


class MaterialCompanyUpdateView(CustomGenericUpdateView):
    serializer_class = MaterialCompanyUpdateSerializer
    queryset = MaterialCompany.objects.all()
    success_response_message = "Material Company updated successfully."
