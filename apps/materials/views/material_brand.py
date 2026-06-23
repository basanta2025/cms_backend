from base.views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import MaterialBrand
from ..serializers import (
    MaterialBrandCreateSerializer,
    MaterialBrandListSerializer,
    MaterialBrandRetrieveSerializer,
    MaterialBrandUpdateSerializer,
)


class MaterialBrandCreateView(CustomGenericCreateView):
    queryset = MaterialBrand.objects.all()
    serializer_class = MaterialBrandCreateSerializer
    success_response_message = "Material Brand created successfully."


class MaterialBrandListView(CustomGenericListView):
    queryset = MaterialBrand.objects.all()
    serializer_class = MaterialBrandListSerializer
    success_response_message = "Material Brand fetched successfully."


class MaterialBrandRetrieveView(CustomGenericRetrieveView):
    queryset = MaterialBrand.objects.all()
    serializer_class = MaterialBrandRetrieveSerializer
    success_response_message = "Material Brand retrieved successfully."


class MaterialBrandUpdateView(CustomGenericUpdateView):
    queryset = MaterialBrand.objects.all()
    serializer_class = MaterialBrandUpdateSerializer
    success_response_message = "Material Brand updated successfully."
