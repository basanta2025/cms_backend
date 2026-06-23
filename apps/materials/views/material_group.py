from base.views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import MaterialGroup
from ..serializers import (
    MaterialGroupCreateSerializer,
    MaterialGroupListSerializer,
    MaterialGroupRetrieveSerializer,
    MaterialGroupUpdateSerializer,
)


class MaterialGroupCreateView(CustomGenericCreateView):
    queryset = MaterialGroup.objects.all()
    serializer_class = MaterialGroupCreateSerializer
    success_response_message = "Material Group created successfully."


class MaterialGroupListView(CustomGenericListView):
    queryset = MaterialGroup.objects.all()
    serializer_class = MaterialGroupListSerializer
    success_response_message = "Material Group fetched successfully."


class MaterialGroupRetrieveView(CustomGenericRetrieveView):
    queryset = MaterialGroup.objects.all()
    serializer_class = MaterialGroupRetrieveSerializer
    success_response_message = "Material Group retrieved successfully."


class MaterialGroupUpdateView(CustomGenericUpdateView):
    queryset = MaterialGroup.objects.all()
    serializer_class = MaterialGroupUpdateSerializer
    success_response_message = "Material Group updated successfully."
