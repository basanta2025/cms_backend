from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import TaskMaterial
from ..serializers import (
    TaskMaterialCreateSerializer,
    TaskMaterialListSerializer,
    TaskMaterialRetrieveSerializer,
    TaskMaterialUpdateSerializer,
)


class TaskMaterialListView(CustomGenericListView):
    serializer_class = TaskMaterialListSerializer
    queryset = TaskMaterial.objects.all()
    success_response_message = "Task Material fetched successfully."


class TaskMaterialCreateView(CustomGenericCreateView):
    serializer_class = TaskMaterialCreateSerializer
    queryset = TaskMaterial.objects.all()
    success_response_message = "Task Material created successfully."


class TaskMaterialRetrieveView(CustomGenericRetrieveView):
    serializer_class = TaskMaterialRetrieveSerializer
    queryset = TaskMaterial.objects.all()
    success_response_message = "Task Material retrieved successfully."


class TaskMaterialUpdateView(CustomGenericUpdateView):
    serializer_class = TaskMaterialUpdateSerializer
    queryset = TaskMaterial.objects.all()
    success_response_message = "Task Material updated successfully."
