from base.views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import MaterialType
from ..serializers import (
    MaterialTypeCreateSerializer,
    MaterialTypeListSerializer,
    MaterialTypeRetrieveSerializer,
    MaterialTypeUpdateSerializer,
)


class MaterialTypeCreateView(CustomGenericCreateView):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeCreateSerializer
    success_response_message = "Material Type created successfully."


class MaterialTypeListView(CustomGenericListView):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeListSerializer
    success_response_message = "Material Type fetched successfully."


class MaterialTypeRetrieveView(CustomGenericRetrieveView):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeRetrieveSerializer
    success_response_message = "Material Type retrieved successfully."


class MaterialTypeUpdateView(CustomGenericUpdateView):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeUpdateSerializer
    success_response_message = "Material Type updated successfully."
