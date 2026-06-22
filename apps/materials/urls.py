from django.urls import include, path

from .views import (
    MaterialCategoryCreateView,
    MaterialCategoryListView,
    MaterialCategoryRetrieveView,
    MaterialCategoryUpdateView,
    MaterialCreateView,
    MaterialListView,
    MaterialRetrieveView,
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

urlpatterns = [
    path("material-category/", include(material_category_patterns)),
    path("material/", include(material_patterns)),
    path("project-material/", include(project_material_patterns)),
    path("task-material/", include(task_material_patterns)),
]
