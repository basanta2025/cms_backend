from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import Project


class ProjectCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Project
        exclude = ExcludeFields.exclude


class ProjectListSerializer(BaseModelSerializer):
    class Meta:
        model = Project
        exclude = ExcludeFields.exclude


class ProjectRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = Project
        exclude = ExcludeFields.exclude


class ProjectUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = Project
        exclude = ExcludeFields.exclude
