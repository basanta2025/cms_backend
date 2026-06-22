from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import Project
from ..serializers import (
    ProjectCreateSerializer,
    ProjectListSerializer,
    ProjectRetrieveSerializer,
    ProjectUpdateSerializer,
)


class ProjectCreateView(CustomGenericCreateView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    success_message = "Project created successfully."


class ProjectListView(CustomGenericListView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    success_message = "Project fetched successfully."


class ProjectRetrieveView(CustomGenericRetrieveView):
    queryset = Project.objects.all()
    serializer_class = ProjectRetrieveSerializer
    success_message = "Project retrieved successfully."


class ProjectUpdateView(CustomGenericUpdateView):
    queryset = Project.objects.all()
    serializer_class = ProjectUpdateSerializer
    success_message = "Project updated successfully."
