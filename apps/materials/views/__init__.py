from .base_unit import (
    BaseUnitCreateView,
    BaseUnitDropdownListView,
    BaseUnitListView,
    BaseUnitRetrieveView,
    BaseUnitUpdateView,
)
from .material_brand import (
    MaterialBrandCreateView,
    MaterialBrandListView,
    MaterialBrandRetrieveView,
    MaterialBrandUpdateView,
)
from .material_colour import (
    MaterialColourCreateView,
    MaterialColourListView,
    MaterialColourRetrieveView,
    MaterialColourUpdateView,
)
from .material_company import (
    MaterialCompanyCreateView,
    MaterialCompanyListView,
    MaterialCompanyRetrieveView,
    MaterialCompanyUpdateView,
)
from .material_group import (
    MaterialGroupCreateView,
    MaterialGroupListView,
    MaterialGroupRetrieveView,
    MaterialGroupUpdateView,
)
from .material_shape import (
    MaterialShapeCreateView,
    MaterialShapeListView,
    MaterialShapeRetrieveView,
    MaterialShapeUpdateView,
)
from .material_type import (
    MaterialTypeCreateView,
    MaterialTypeListView,
    MaterialTypeRetrieveView,
    MaterialTypeUpdateView,
)
from .materials import (
    MaterialCategoryCreateView,
    MaterialCategoryListView,
    MaterialCategoryRetrieveView,
    MaterialCategoryUpdateView,
    MaterialCreateView,
    MaterialListView,
    MaterialRetrieveView,
    MaterialUpdateView,
)
from .project_materials import (
    ProjectMaterialCreateView,
    ProjectMaterialListView,
    ProjectMaterialRetrieveView,
    ProjectMaterialUpdateView,
)
from .task_materials import (
    TaskMaterialCreateView,
    TaskMaterialListView,
    TaskMaterialRetrieveView,
    TaskMaterialUpdateView,
)

__all__ = [
    # material-category-view
    "MaterialCategoryCreateView",
    "MaterialCategoryListView",
    "MaterialCategoryRetrieveView",
    "MaterialCategoryUpdateView",
    # material-view
    "MaterialCreateView",
    "MaterialListView",
    "MaterialRetrieveView",
    "MaterialUpdateView",
    # project-material-view
    "ProjectMaterialCreateView",
    "ProjectMaterialListView",
    "ProjectMaterialRetrieveView",
    "ProjectMaterialUpdateView",
    # task-material-view
    "TaskMaterialCreateView",
    "TaskMaterialListView",
    "TaskMaterialRetrieveView",
    "TaskMaterialUpdateView",
    # base-unit-view
    "BaseUnitCreateView",
    "BaseUnitDropdownListView",
    "BaseUnitListView",
    "BaseUnitRetrieveView",
    "BaseUnitUpdateView",
    #  .material_brand
    "MaterialBrandCreateView",
    "MaterialBrandListView",
    "MaterialBrandRetrieveView",
    "MaterialBrandUpdateView",
    # material_colour
    "MaterialColourCreateView",
    "MaterialColourListView",
    "MaterialColourRetrieveView",
    "MaterialColourUpdateView",
    # material_company
    "MaterialCompanyCreateView",
    "MaterialCompanyListView",
    "MaterialCompanyRetrieveView",
    "MaterialCompanyUpdateView",
    # material_group
    "MaterialGroupCreateView",
    "MaterialGroupListView",
    "MaterialGroupRetrieveView",
    "MaterialGroupUpdateView",
    #  material_shape
    "MaterialShapeCreateView",
    "MaterialShapeListView",
    "MaterialShapeRetrieveView",
    "MaterialShapeUpdateView",
    # material_type
    "MaterialTypeCreateView",
    "MaterialTypeListView",
    "MaterialTypeRetrieveView",
    "MaterialTypeUpdateView",
]
