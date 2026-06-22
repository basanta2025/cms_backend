from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import ProjectMaterial
from ..serializers import (
    ProjectMaterialCreateSerializer,
    ProjectMaterialListSerializer,
    ProjectMaterialRetrieveSerializer,
    ProjectMaterialUpdateSerializer,
)


class ProjectMaterialListView(CustomGenericListView):
    serializer_class = ProjectMaterialListSerializer
    queryset = ProjectMaterial.objects.all()
    success_response_message = "Project Material fetched successfully."


class ProjectMaterialCreateView(CustomGenericCreateView):
    serializer_class = ProjectMaterialCreateSerializer
    queryset = ProjectMaterial.objects.all()
    success_response_message = "Project Material created successfully."


class ProjectMaterialRetrieveView(CustomGenericRetrieveView):
    serializer_class = ProjectMaterialRetrieveSerializer
    queryset = ProjectMaterial.objects.all()
    success_response_message = "Project Material retrieved successfully."


class ProjectMaterialUpdateView(CustomGenericUpdateView):
    serializer_class = ProjectMaterialUpdateSerializer
    queryset = ProjectMaterial.objects.all()
    success_response_message = "Project Material updated successfully."
