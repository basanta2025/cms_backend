from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import MaterialShape


class MaterialShapeCreateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialShape
        exclude = ExcludeFields.exclude


class MaterialShapeListSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialShape
        exclude = ExcludeFields.exclude


class MaterialShapeRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialShape
        exclude = ExcludeFields.exclude


class MaterialShapeUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialShape
        exclude = ExcludeFields.exclude
