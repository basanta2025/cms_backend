from django.urls import include, path

from .views import (
    BaseUnitCreateView,
    BaseUnitDropdownListView,
    BaseUnitListView,
    BaseUnitRetrieveView,
    BaseUnitUpdateView,
    MaterialBrandCreateView,
    MaterialBrandListView,
    MaterialBrandRetrieveView,
    MaterialBrandUpdateView,
    MaterialCategoryCreateView,
    MaterialCategoryListView,
    MaterialCategoryRetrieveView,
    MaterialCategoryUpdateView,
    MaterialColourCreateView,
    MaterialColourListView,
    MaterialColourRetrieveView,
    MaterialColourUpdateView,
    MaterialCompanyCreateView,
    MaterialCompanyListView,
    MaterialCompanyRetrieveView,
    MaterialCompanyUpdateView,
    MaterialCreateView,
    MaterialGroupCreateView,
    MaterialGroupListView,
    MaterialGroupRetrieveView,
    MaterialGroupUpdateView,
    MaterialListView,
    MaterialRetrieveView,
    MaterialShapeCreateView,
    MaterialShapeListView,
    MaterialShapeRetrieveView,
    MaterialShapeUpdateView,
    MaterialTypeCreateView,
    MaterialTypeListView,
    MaterialTypeRetrieveView,
    MaterialTypeUpdateView,
    MaterialUpdateView,
    ProjectMaterialCreateView,
    ProjectMaterialListView,
    ProjectMaterialRetrieveView,
    ProjectMaterialUpdateView,
    TaskMaterialCreateView,
    TaskMaterialListView,
    TaskMaterialRetrieveView,
    TaskMaterialUpdateView,
)

material_category_patterns = [
    path(
        "create", MaterialCategoryCreateView.as_view(), name="material-category-create"
    ),
    path("list", MaterialCategoryListView.as_view(), name="material-category-list"),
    path(
        "retrieve/<int:pk>",
        MaterialCategoryRetrieveView.as_view(),
        name="material-category-retrieve",
    ),
    path(
        "update/<int:pk>",
        MaterialCategoryUpdateView.as_view(),
        name="material-category-create",
    ),
]
material_patterns = [
    path("create", MaterialCreateView.as_view(), name="material-create"),
    path("list", MaterialListView.as_view(), name="material-list"),
    path("retrieve/<int:pk>", MaterialRetrieveView.as_view(), name="material-retrieve"),
    path("update/<int:pk>", MaterialUpdateView.as_view(), name="material-update"),
]
project_material_patterns = [
    path("create", ProjectMaterialCreateView.as_view(), name="project-material-create"),
    path("list", ProjectMaterialListView.as_view(), name="project-material-list"),
    path(
        "retrieve/<int:pk>",
        ProjectMaterialRetrieveView.as_view(),
        name="project-material-retrieve",
    ),
    path(
        "update/<int:pk>",
        ProjectMaterialUpdateView.as_view(),
        name="project-material-update",
    ),
]
task_material_patterns = [
    path("create", TaskMaterialCreateView.as_view(), name="task-material-create"),
    path("list", TaskMaterialListView.as_view(), name="task-material-list"),
    path(
        "retrieve/<int:pk>",
        TaskMaterialRetrieveView.as_view(),
        name="task-material-retrieve",
    ),
    path(
        "update/<int:pk>",
        TaskMaterialUpdateView.as_view(),
        name="task-material-update",
    ),
]


base_unit_patterns = [
    path("create", BaseUnitCreateView.as_view(), name="base-unit-create"),
    path("list", BaseUnitListView.as_view(), name="base-unit-list"),
    path(
        "retrieve/<int:pk>", BaseUnitRetrieveView.as_view(), name="base-unit-retrieve"
    ),
    path("update/<int:pk>", BaseUnitUpdateView.as_view(), name="base-unit-update"),
]
material_brand_patterns = [
    path("create", MaterialBrandCreateView.as_view(), name="material-brand-create"),
    path("list", MaterialBrandListView.as_view(), name="material-brand-list"),
    path(
        "retrieve/<int:pk>",
        MaterialBrandRetrieveView.as_view(),
        name="material-brand-retrieve",
    ),
    path(
        "update/<int:pk>",
        MaterialBrandUpdateView.as_view(),
        name="material-brand-update",
    ),
]
material_colour_patterns = [
    path("create", MaterialColourCreateView.as_view(), name="material-colour-create"),
    path("list", MaterialColourListView.as_view(), name="material-colour-list"),
    path(
        "retrieve/<int:pk>",
        MaterialColourRetrieveView.as_view(),
        name="material-colour-retrieve",
    ),
    path(
        "update/<int:pk>",
        MaterialColourUpdateView.as_view(),
        name="material-colour-update",
    ),
]
material_company_patterns = [
    path("create", MaterialCompanyCreateView.as_view(), name="material-company-create"),
    path("list", MaterialCompanyListView.as_view(), name="material-company-list"),
    path(
        "retrieve/<int:pk>",
        MaterialCompanyRetrieveView.as_view(),
        name="material-company-retrieve",
    ),
    path(
        "update/<int:pk>",
        MaterialCompanyUpdateView.as_view(),
        name="material-company-update",
    ),
]
material_shape_patterns = [
    path("create", MaterialShapeCreateView.as_view(), name="material-shape-create"),
    path("list", MaterialShapeListView.as_view(), name="material-shape-list"),
    path(
        "retrieve/<int:pk>",
        MaterialShapeRetrieveView.as_view(),
        name="material-shape-retrieve",
    ),
    path(
        "update/<int:pk>",
        MaterialShapeUpdateView.as_view(),
        name="material-shape-update",
    ),
]
material_type_patterns = [
    path("create", MaterialTypeCreateView.as_view(), name="material-type-create"),
    path("list", MaterialTypeListView.as_view(), name="material-type-list"),
    path(
        "retrieve/<int:pk>",
        MaterialTypeRetrieveView.as_view(),
        name="material-type-retrieve",
    ),
    path(
        "update/<int:pk>",
        MaterialTypeUpdateView.as_view(),
        name="material-type-update",
    ),
]
material_group_patterns = [
    path("create", MaterialGroupCreateView.as_view(), name="material-group-create"),
    path("list", MaterialGroupListView.as_view(), name="material-group-list"),
    path(
        "retrieve/<int:pk>",
        MaterialGroupRetrieveView.as_view(),
        name="material-group-retrieve",
    ),
    path(
        "update/<int:pk>",
        MaterialGroupUpdateView.as_view(),
        name="material-group-update",
    ),
]
urlpatterns = [
    path("material-category/", include(material_category_patterns)),
    path("material/", include(material_patterns)),
    path("project-material/", include(project_material_patterns)),
    path("task-material/", include(task_material_patterns)),
    path("material-shape/", include(material_shape_patterns)),
    path("material-type/", include(material_type_patterns)),
    path("material-group/", include(material_group_patterns)),
    path("base-unit/", include(base_unit_patterns)),
    path("material-brand/", include(material_brand_patterns)),
    path("material-colour/", include(material_colour_patterns)),
    path("material-company/", include(material_company_patterns)),
]
