from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import MaterialGroup


class MaterialGroupCreateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialGroup
        exclude = ExcludeFields.exclude


class MaterialGroupListSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialGroup
        exclude = ExcludeFields.exclude


class MaterialGroupRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialGroup
        exclude = ExcludeFields.exclude


class MaterialGroupUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialGroup
        exclude = ExcludeFields.exclude
