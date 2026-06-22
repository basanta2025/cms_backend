from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import Task
from ..serializers import (
    TaskCreateSerializer,
    TaskListSerializer,
    TaskRetrieveSerializer,
    TaskUpdateSerializer,
)


class TaskCreateView(CustomGenericCreateView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    success_message = "Task created successfully."


class TaskListView(CustomGenericListView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    success_message = "Tasks fetched successfully."


class TaskRetrieveView(CustomGenericRetrieveView):
    queryset = Task.objects.all()
    serializer_class = TaskRetrieveSerializer
    success_message = "Task retrieved successfully."


class TaskUpdateView(CustomGenericUpdateView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    success_message = "Task updated successfully."
