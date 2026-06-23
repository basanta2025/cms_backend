from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import MaterialBrand


class MaterialBrandCreateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialBrand
        exclude = ExcludeFields.exclude


class MaterialBrandListSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialBrand
        exclude = ExcludeFields.exclude


class MaterialBrandRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialBrand
        exclude = ExcludeFields.exclude


class MaterialBrandUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialBrand
        exclude = ExcludeFields.exclude
