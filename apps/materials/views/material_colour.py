from base.views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import MaterialColour
from ..serializers import (
    MaterialColourCreateSerializer,
    MaterialColourListSerializer,
    MaterialColourRetrieveSerializer,
    MaterialColourUpdateSerializer,
)


class MaterialColourCreateView(CustomGenericCreateView):
    queryset = MaterialColour.objects.all()
    serializer_class = MaterialColourCreateSerializer
    success_response_message = "Material Colour created successfully."


class MaterialColourListView(CustomGenericListView):
    queryset = MaterialColour.objects.all()
    serializer_class = MaterialColourListSerializer
    success_response_message = "Material Colour fetched successfully."


class MaterialColourRetrieveView(CustomGenericRetrieveView):
    queryset = MaterialColour.objects.all()
    serializer_class = MaterialColourRetrieveSerializer
    success_response_message = "Material Colour retrieved successfully."


class MaterialColourUpdateView(CustomGenericUpdateView):
    queryset = MaterialColour.objects.all()
    serializer_class = MaterialColourUpdateSerializer
    success_response_message = "Material Colour updated successfully."
    success_response_message = "Material Colour created successfully."
