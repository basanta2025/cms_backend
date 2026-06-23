from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import MaterialType


class MaterialTypeCreateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialType
        exclude = ExcludeFields.exclude


class MaterialTypeListSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialType
        exclude = ExcludeFields.exclude


class MaterialTypeRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialType
        exclude = ExcludeFields.exclude


class MaterialTypeUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialType
        exclude = ExcludeFields.exclude
