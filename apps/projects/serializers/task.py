from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import Task


class TaskCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Task
        exclude = ExcludeFields.exclude


class TaskListSerializer(BaseModelSerializer):
    class Meta:
        model = Task
        exclude = ExcludeFields.exclude


class TaskRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = Task
        exclude = ExcludeFields.exclude


class TaskUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = Task
        exclude = ExcludeFields.exclude
