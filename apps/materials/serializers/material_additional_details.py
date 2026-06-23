from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import MaterialAdditionalDetails
from .base_unit import BaseUnitDropdownSerializer
from .material_brand import MaterialBrandRetrieveSerializer
from .material_company import MaterialCompanyRetrieveSerializer
from .material_shape import MaterialShapeRetrieveSerializer
from .material_type import MaterialTypeRetrieveSerializer


class MaterialAdditionalDetailsCreateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialAdditionalDetails
        exclude = ExcludeFields.exclude


class MaterialAdditionalDetailsForMaterialListSerializer(BaseModelSerializer):
    brand = MaterialBrandRetrieveSerializer(read_only=True)
    company = MaterialCompanyRetrieveSerializer(read_only=True)
    shape = MaterialShapeRetrieveSerializer(read_only=True)
    type = MaterialTypeRetrieveSerializer(read_only=True)

    class Meta:
        model = MaterialAdditionalDetails
        exclude = ExcludeFields.exclude


class MaterialAdditionalDetailsForMaterialRetrieveSerializer(BaseModelSerializer):
    brand = MaterialBrandRetrieveSerializer(read_only=True)
    company = MaterialCompanyRetrieveSerializer(read_only=True)
    shape = MaterialShapeRetrieveSerializer(read_only=True)
    type = MaterialTypeRetrieveSerializer(read_only=True)
    excise_unit = BaseUnitDropdownSerializer(read_only=True)
    purchase_unit = BaseUnitDropdownSerializer(read_only=True)
    purchase_cost_unit = BaseUnitDropdownSerializer(read_only=True)

    class Meta:
        model = MaterialAdditionalDetails
        exclude = ExcludeFields.exclude


class MaterialAdditionalDetailsUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialAdditionalDetails
        exclude = ExcludeFields.exclude


class MaterialAdditionalDetailsForMaterialCreateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialAdditionalDetails
        exclude = ExcludeFields.exclude + [
            "material",
        ]


class MaterialAdditionalDetailsForMaterialUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = MaterialAdditionalDetails
        exclude = ExcludeFields.exclude + [
            "material",
        ]
