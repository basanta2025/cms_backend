from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import VendorFinancialDetail


class VendorFinancialDetailCreateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorFinancialDetail
        exclude = ExcludeFields.exclude


class VendorFinancialDetailListSerializer(BaseModelSerializer):
    class Meta:
        model = VendorFinancialDetail
        exclude = ExcludeFields.exclude


class VendorFinancialDetailUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorFinancialDetail
        exclude = ExcludeFields.exclude


class VendorFinancialDetailRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = VendorFinancialDetail
        exclude = ExcludeFields.exclude
