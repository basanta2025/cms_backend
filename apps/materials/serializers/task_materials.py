from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import TaskMaterial


class TaskMaterialListSerializer(BaseModelSerializer):
    class Meta:
        model = TaskMaterial
        exclude = ExcludeFields.exclude


class TaskMaterialCreateSerializer(BaseModelSerializer):
    class Meta:
        model = TaskMaterial
        exclude = ExcludeFields.exclude


class TaskMaterialRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = TaskMaterial
        exclude = ExcludeFields.exclude


class TaskMaterialUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = TaskMaterial
        exclude = ExcludeFields.exclude
