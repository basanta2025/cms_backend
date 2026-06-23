from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import MaterialCompany


class MaterialCompanyCreateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialCompany
        exclude = ExcludeFields.exclude


class MaterialCompanyListSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialCompany
        exclude = ExcludeFields.exclude


class MaterialCompanyRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialCompany
        exclude = ExcludeFields.exclude


class MaterialCompanyUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialCompany
        exclude = ExcludeFields.exclude
