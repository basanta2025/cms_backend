from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import VendorBankAccount


class VendorBankAccountCreateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorBankAccount
        exclude = ExcludeFields.exclude


class VendorBankAccountListSerializer(BaseModelSerializer):
    class Meta:
        model = VendorBankAccount
        exclude = ExcludeFields.exclude


class VendorBankAccountUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorBankAccount
        exclude = ExcludeFields.exclude


class VendorBankAccountRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = VendorBankAccount
        exclude = ExcludeFields.exclude
