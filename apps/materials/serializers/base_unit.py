from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from base.serializers import BaseModelSerializer, ExcludeFields, ReadOnlyFields

from ..models import BaseUnit


class ParentBaseUnitForMethodSerializer(BaseModelSerializer):
    class Meta:
        model = BaseUnit
        exclude = ExcludeFields.exclude


class BaseUnitSerializer(BaseModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = BaseUnit
        fields = "__all__"
        # exclude = ExcludeFields.exclude + ["lft", "rght", "level", "tree_id"]

    @extend_schema_field(ParentBaseUnitForMethodSerializer)
    def get_parent(self, obj):
        """
        Return the nested parent as serialized data, or None if no parent exists.
        """
        if obj.parent:
            return BaseUnitSerializer(obj.parent, context=self.context).data
        return None


class BaseUnitForConversionView(BaseModelSerializer):
    class Meta:
        model = BaseUnit
        exclude = ExcludeFields.exclude + ["lft", "rght", "level", "tree_id"]


class BaseUnitDropdownSerializer(BaseModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = BaseUnit
        fields = [
            "id",
            "name",
            "parent",
        ]

    @extend_schema_field(ParentBaseUnitForMethodSerializer)
    def get_parent(self, obj):
        """
        Return the nested parent as serialized data, or None if no parent exists.
        """
        if obj.parent:
            return BaseUnitDropdownSerializer(obj.parent, context=self.context).data
        return None


class BaseUnitCreateSerializer(BaseModelSerializer):
    class Meta:
        model = BaseUnit
        exclude = ExcludeFields.exclude


class BaseUnitUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = BaseUnit
        # exclude = ExcludeFields.exclude
        fields = "__all__"
        read_only_fields = ReadOnlyFields.read_only
