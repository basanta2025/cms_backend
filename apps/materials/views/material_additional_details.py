from base.views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..filters import MaterialAdditionalDetailsFilter
from ..models import MaterialAdditionalDetails
from ..serializers import (
    MaterialAdditionalDetailsCreateSerializer,
    MaterialAdditionalDetailsForMaterialListSerializer,
    MaterialAdditionalDetailsForMaterialRetrieveSerializer,
    MaterialAdditionalDetailsUpdateSerializer,
)


class MaterialAdditionalDetailsListView(CustomGenericListView):
    queryset = MaterialAdditionalDetails.objects.all().select_related(
        # Material
        "material",
        "material__group",
        "material__base_unit",
        "material__category",
        "material__material_type",
        "brand",
        "colour",
        "shape",
        "company_name",
        "excise_unit",
        "purchase_unit",
        "purchase_cost_unit",
        "sale_unit",
        "sale_cost_unit",
    )
    serializer_class = MaterialAdditionalDetailsForMaterialListSerializer
    success_response_message = "Material Additional details fetched successfully."
    permission_classes = []
    search_fields = ["name"]
    filterset_class = MaterialAdditionalDetailsFilter


class MaterialAdditionalDetailsRetrieveView(CustomGenericRetrieveView):
    queryset = MaterialAdditionalDetails.objects.all().select_related(
        "material",
        "brand",
        "colour",
        "shape",
        "company_name",
        "excise_unit",
        "purchase_unit",
        "purchase_cost_unit",
    )
    serializer_class = MaterialAdditionalDetailsForMaterialRetrieveSerializer
    permission_classes = []
    search_fields = ["name"]
    success_response_message = "Material Additional details retrieved successfully."


class MaterialAdditionalDetailsCreateView(CustomGenericCreateView):
    queryset = MaterialAdditionalDetails.objects.all()
    serializer_class = MaterialAdditionalDetailsCreateSerializer
    permission_classes = []
    search_fields = ["name"]
    success_response_message = "Material Additional details created successfully."


class MaterialAdditionalDetailsUpdateView(CustomGenericUpdateView):
    queryset = MaterialAdditionalDetails.objects.all()
    serializer_class = MaterialAdditionalDetailsUpdateSerializer
    permission_classes = []
    search_fields = ["name"]
    success_response_message = "Material Additional details updated successfully."
