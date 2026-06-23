from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import MaterialColour


class MaterialColourCreateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialColour
        exclude = ExcludeFields.exclude


class MaterialColourListSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialColour
        exclude = ExcludeFields.exclude


class MaterialColourRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialColour
        exclude = ExcludeFields.exclude


class MaterialColourUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialColour
        exclude = ExcludeFields.exclude
