from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import VendorDocument


class VendorDocumentCreateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorDocument
        exclude = ExcludeFields.exclude


class VendorDocumentListSerializer(BaseModelSerializer):
    class Meta:
        model = VendorDocument
        exclude = ExcludeFields.exclude


class VendorDocumentUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = VendorDocument
        exclude = ExcludeFields.exclude


class VendorDocumentRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = VendorDocument
        exclude = ExcludeFields.exclude
