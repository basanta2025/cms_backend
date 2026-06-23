from .base_unit import (
    BaseUnitCreateSerializer,
    BaseUnitDropdownSerializer,
    BaseUnitForConversionView,
    BaseUnitSerializer,
    BaseUnitUpdateSerializer,
)
from .material_additional_details import (
    MaterialAdditionalDetailsCreateSerializer,
    MaterialAdditionalDetailsForMaterialCreateSerializer,
    MaterialAdditionalDetailsForMaterialListSerializer,
    MaterialAdditionalDetailsForMaterialRetrieveSerializer,
    MaterialAdditionalDetailsForMaterialUpdateSerializer,
    MaterialAdditionalDetailsUpdateSerializer,
)
from .material_brand import (
    MaterialBrandCreateSerializer,
    MaterialBrandListSerializer,
    MaterialBrandRetrieveSerializer,
    MaterialBrandUpdateSerializer,
)
from .material_colour import (
    MaterialColourCreateSerializer,
    MaterialColourListSerializer,
    MaterialColourRetrieveSerializer,
    MaterialColourUpdateSerializer,
)
from .material_company import (
    MaterialCompanyCreateSerializer,
    MaterialCompanyListSerializer,
    MaterialCompanyRetrieveSerializer,
    MaterialCompanyUpdateSerializer,
)
from .material_group import (
    MaterialGroupCreateSerializer,
    MaterialGroupListSerializer,
    MaterialGroupRetrieveSerializer,
    MaterialGroupUpdateSerializer,
)
from .material_shape import (
    MaterialShapeCreateSerializer,
    MaterialShapeListSerializer,
    MaterialShapeRetrieveSerializer,
    MaterialShapeUpdateSerializer,
)
from .material_type import (
    MaterialTypeCreateSerializer,
    MaterialTypeListSerializer,
    MaterialTypeRetrieveSerializer,
    MaterialTypeUpdateSerializer,
)
from .materials import (
    MaterialCategoryCreateSerializer,
    MaterialCategoryListSerializer,
    MaterialCategoryRetrieveSerializer,
    MaterialCategoryUpdateSerializer,
    MaterialCreateSerializer,
    MaterialListSerializer,
    MaterialRetrieveSerializer,
    MaterialUpdateSerializer,
)
from .project_materials import (
    ProjectMaterialCreateSerializer,
    ProjectMaterialListSerializer,
    ProjectMaterialRetrieveSerializer,
    ProjectMaterialUpdateSerializer,
)
from .task_materials import (
    TaskMaterialCreateSerializer,
    TaskMaterialListSerializer,
    TaskMaterialRetrieveSerializer,
    TaskMaterialUpdateSerializer,
)

# MaterialAdditionalDetailsForMaterialRetrieveSerializer,
# MaterialAdditionalDetailsForMaterialUpdateSerializer,

__all__ = [
    # Material Category Serializers - -
    "MaterialCategoryCreateSerializer",
    "MaterialCategoryListSerializer",
    "MaterialCategoryRetrieveSerializer",
    "MaterialCategoryUpdateSerializer",
    # Material Serializers - -
    "MaterialCreateSerializer",
    "MaterialListSerializer",
    "MaterialRetrieveSerializer",
    "MaterialUpdateSerializer",
    # Project Material Serializers - -
    "ProjectMaterialCreateSerializer",
    "ProjectMaterialListSerializer",
    "ProjectMaterialRetrieveSerializer",
    "ProjectMaterialUpdateSerializer",
    # Task Material Serializers - -
    "TaskMaterialCreateSerializer",
    "TaskMaterialListSerializer",
    "TaskMaterialRetrieveSerializer",
    "TaskMaterialUpdateSerializer",
    # Base Unit Serializers - -
    "BaseUnitCreateSerializer",
    "BaseUnitDropdownSerializer",
    "BaseUnitForConversionView",
    "BaseUnitSerializer",
    "BaseUnitUpdateSerializer",
    # Material Additional Details Serializers - -
    "MaterialAdditionalDetailsCreateSerializer",
    "MaterialAdditionalDetailsUpdateSerializer",
    # Material Additional Details Serializers for Material - -
    "MaterialAdditionalDetailsForMaterialCreateSerializer",
    "MaterialAdditionalDetailsForMaterialListSerializer",
    "MaterialAdditionalDetailsForMaterialRetrieveSerializer",
    "MaterialAdditionalDetailsForMaterialUpdateSerializer",
    # Material Brand Serializers - -
    "MaterialBrandCreateSerializer",
    "MaterialBrandListSerializer",
    "MaterialBrandRetrieveSerializer",
    "MaterialBrandUpdateSerializer",
    # Material Colour Serializers - -
    "MaterialColourCreateSerializer",
    "MaterialColourListSerializer",
    "MaterialColourRetrieveSerializer",
    "MaterialColourUpdateSerializer",
    # MaterialAdditionalDetailsForMaterialRetrieveSerializer,
    # MaterialAdditionalDetailsForMaterialUpdateSerializer,
    # Material Company Serializers - -
    "MaterialCompanyCreateSerializer",
    "MaterialCompanyListSerializer",
    "MaterialCompanyRetrieveSerializer",
    "MaterialCompanyUpdateSerializer",
    # Material Group Serializers - -
    "MaterialGroupCreateSerializer",
    "MaterialGroupListSerializer",
    "MaterialGroupRetrieveSerializer",
    "MaterialGroupUpdateSerializer",
    # Material Shape Serializers - -
    "MaterialShapeCreateSerializer",
    "MaterialShapeListSerializer",
    "MaterialShapeRetrieveSerializer",
    "MaterialShapeUpdateSerializer",
    # Material Type Serializers - -
    "MaterialTypeCreateSerializer",
    "MaterialTypeListSerializer",
    "MaterialTypeRetrieveSerializer",
    "MaterialTypeUpdateSerializer",
]
