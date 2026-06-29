from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import Vendor


class VendorCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Vendor
        exclude = ExcludeFields.exclude


class VendorListSerializer(BaseModelSerializer):
    class Meta:
        model = Vendor
        exclude = ExcludeFields.exclude


class VendorUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = Vendor
        exclude = ExcludeFields.exclude


class VendorRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = Vendor
        exclude = ExcludeFields.exclude
