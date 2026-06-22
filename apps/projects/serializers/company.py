from base.serializers import BaseModelSerializer, ExcludeFields, serializers

from ..models import Company


class CompanyCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Company
        exclude = ExcludeFields.exclude


class CompanyListSerializer(BaseModelSerializer):
    class Meta:
        model = Company
        exclude = ExcludeFields.exclude


class CompanyRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = Company
        exclude = ExcludeFields.exclude


class CompanyUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = Company
        exclude = ExcludeFields.exclude
