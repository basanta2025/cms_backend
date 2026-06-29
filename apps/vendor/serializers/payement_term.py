from base.serializers import BaseModelSerializer, ExcludeFields

from ..models.vendor_details import VendorPaymentTerm


class VendorPaymentTermCreateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorPaymentTerm
        exclude = ExcludeFields.exclude


class VendorPaymentTermListSerializer(BaseModelSerializer):
    class Meta:
        model = VendorPaymentTerm
        exclude = ExcludeFields.exclude


class VendorPaymentTermUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorPaymentTerm
        exclude = ExcludeFields.exclude


class VendorPaymentTermRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = VendorPaymentTerm
        exclude = ExcludeFields.exclude
