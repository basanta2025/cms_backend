from .company import (
    CompanyCreateView,
    CompanyListView,
    CompanyRetrieveView,
    CompanyUpdateView,
)
from .document import (
    DocumentCreateView,
    DocumentListView,
    DocumentRetrieveView,
    DocumentUpdateView,
)
from .milestone import (
    MilestoneCreateView,
    MilestoneListView,
    MilestoneRetrieveView,
    MilestoneUpdateView,
)
from .project_budget import (
    BudgetCategoryCreateView,
    BudgetCategoryListView,
    BudgetCategoryRetrieveView,
    BudgetCategoryUpdateView,
    ProjectBudgetCreateView,
    ProjectBudgetListView,
    ProjectBudgetRetrieveView,
    ProjectBudgetUpdateView,
)
from .projects import (
    ProjectCreateView,
    ProjectListView,
    ProjectRetrieveView,
    ProjectUpdateView,
)
from .task import (
    TaskCreateView,
    TaskListView,
    TaskRetrieveView,
    TaskUpdateView,
)

__all__ = [
    "CompanyCreateView",
    "CompanyListView",
    "CompanyRetrieveView",
    "CompanyUpdateView",
    # document views
    "DocumentCreateView",
    "DocumentListView",
    "DocumentRetrieveView",
    "DocumentUpdateView",
    # milestone views
    "MilestoneCreateView",
    "MilestoneListView",
    "MilestoneRetrieveView",
    "MilestoneUpdateView",
    # budget category views
    "BudgetCategoryCreateView",
    "BudgetCategoryListView",
    "BudgetCategoryRetrieveView",
    "BudgetCategoryUpdateView",
    "ProjectBudgetCreateView",
    "ProjectBudgetListView",
    "ProjectBudgetRetrieveView",
    "ProjectBudgetUpdateView",
    # project views
    "ProjectCreateView",
    "ProjectListView",
    "ProjectRetrieveView",
    "ProjectUpdateView",
    # task views
    "TaskCreateView",
    "TaskListView",
    "TaskRetrieveView",
    "TaskUpdateView",
]
