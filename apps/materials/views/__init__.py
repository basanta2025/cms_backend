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
]
