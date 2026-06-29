from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import VendorContactPerson


class VendorContactPersonCreateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorContactPerson
        exclude = ExcludeFields.exclude


class VendorContactPersonListSerializer(BaseModelSerializer):
    class Meta:
        model = VendorContactPerson
        exclude = ExcludeFields.exclude


class VendorContactPersonUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorContactPerson
        exclude = ExcludeFields.exclude


class VendorContactPersonRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = VendorContactPerson
        exclude = ExcludeFields.exclude
