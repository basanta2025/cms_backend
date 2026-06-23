from base.views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import MaterialShape
from ..serializers import (
    MaterialShapeCreateSerializer,
    MaterialShapeListSerializer,
    MaterialShapeRetrieveSerializer,
    MaterialShapeUpdateSerializer,
)


class MaterialShapeCreateView(CustomGenericCreateView):
    queryset = MaterialShape.objects.all()
    serializer_class = MaterialShapeCreateSerializer
    success_response_message = "Material Shape created successfully."


class MaterialShapeListView(CustomGenericListView):
    queryset = MaterialShape.objects.all()
    serializer_class = MaterialShapeListSerializer
    success_response_message = "Material Shape fetched successfully."


class MaterialShapeRetrieveView(CustomGenericRetrieveView):
    queryset = MaterialShape.objects.all()
    serializer_class = MaterialShapeRetrieveSerializer
    success_response_message = "Material Shape retrieved successfully."


class MaterialShapeUpdateView(CustomGenericUpdateView):
    queryset = MaterialShape.objects.all()
    serializer_class = MaterialShapeUpdateSerializer
    success_response_message = "Material Shape updated successfully."
