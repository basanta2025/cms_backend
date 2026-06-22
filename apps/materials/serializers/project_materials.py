from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import ProjectMaterial


class ProjectMaterialListSerializer(BaseModelSerializer):
    class Meta:
        model = ProjectMaterial
        exclude = ExcludeFields.exclude


class ProjectMaterialCreateSerializer(BaseModelSerializer):
    class Meta:
        model = ProjectMaterial
        exclude = ExcludeFields.exclude


class ProjectMaterialRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = ProjectMaterial
        exclude = ExcludeFields.exclude


class ProjectMaterialUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = ProjectMaterial
        exclude = ExcludeFields.exclude
