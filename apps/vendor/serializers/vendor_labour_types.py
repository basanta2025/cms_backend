from base.serializers import BaseModelSerializer, ExcludeFields, serializers

from ..models import AttendanceMethodChoices, VendorLabourType, VendorTypeChoices


class VendorLabourTypeCreateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorLabourType
        exclude = ExcludeFields.exclude

    def validate(self, attrs):
        vendor = attrs.get("vendor")

        if vendor.type != VendorTypeChoices.LABOUR:
            raise serializers.ValidationError(
                "Labour types can only be added to vendors of type 'Labour'."
            )

        if vendor.attendance_method != AttendanceMethodChoices.COUNT_OF_WORKERS:
            raise serializers.ValidationError(
                "Labour types can only be added when attendance method is 'Count of Workers'."
            )

        return attrs


class VendorLabourTypeListSerializer(BaseModelSerializer):
    class Meta:
        model = VendorLabourType
        exclude = ExcludeFields.exclude


class VendorLabourTypeUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorLabourType
        exclude = ExcludeFields.exclude


class VendorLabourTypeRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = VendorLabourType
        exclude = ExcludeFields.exclude
