from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import Material, MaterialCategory


# -- Material Category Serializers - -
class MaterialCategoryCreateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialCategory
        exclude = ExcludeFields.exclude


class MaterialCategoryListSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialCategory
        exclude = ExcludeFields.exclude


class MaterialCategoryRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialCategory
        exclude = ExcludeFields.exclude


class MaterialCategoryUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialCategory
        exclude = ExcludeFields.exclude


# -- Material Serializers - -


class MaterialListSerializer(BaseModelSerializer):
    class Meta:
        model = Material
        exclude = ExcludeFields.exclude


class MaterialCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Material
        exclude = ExcludeFields.exclude


class MaterialRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = Material
        exclude = ExcludeFields.exclude


class MaterialUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = Material
        exclude = ExcludeFields.exclude
