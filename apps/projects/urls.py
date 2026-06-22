from django.urls import include, path

from .views import (
    BudgetCategoryCreateView,
    BudgetCategoryListView,
    BudgetCategoryRetrieveView,
    BudgetCategoryUpdateView,
    CompanyCreateView,
    CompanyListView,
    CompanyRetrieveView,
    CompanyUpdateView,
    DocumentCreateView,
    DocumentListView,
    DocumentRetrieveView,
    DocumentUpdateView,
    MilestoneCreateView,
    MilestoneListView,
    MilestoneRetrieveView,
    MilestoneUpdateView,
    ProjectBudgetCreateView,
    ProjectBudgetListView,
    ProjectBudgetRetrieveView,
    ProjectBudgetUpdateView,
    ProjectCreateView,
    ProjectListView,
    ProjectRetrieveView,
    ProjectUpdateView,
    TaskCreateView,
    TaskListView,
    TaskRetrieveView,
    TaskUpdateView,
)

company_patterns = [
    path("create", CompanyCreateView.as_view(), name="company-create"),
    path("list", CompanyListView.as_view(), name="company-list"),
    path("<int:pk>", CompanyRetrieveView.as_view(), name="company-retrieve"),
    path("<int:pk>/update", CompanyUpdateView.as_view(), name="company-update"),
]
document_patterns = [
    path("create", DocumentCreateView.as_view(), name="document-create"),
    path("list", DocumentListView.as_view(), name="document-list"),
    path("<int:pk>", DocumentRetrieveView.as_view(), name="document-retrieve"),
    path("<int:pk>/update", DocumentUpdateView.as_view(), name="document-update"),
]
milestone_patterns = [
    path("create", MilestoneCreateView.as_view(), name="milestone-create"),
    path("list", MilestoneListView.as_view(), name="milestone-list"),
    path("<int:pk>", MilestoneRetrieveView.as_view(), name="milestone-retrieve"),
    path("<int:pk>/update", MilestoneUpdateView.as_view(), name="milestone-update"),
]
budget_category_patterns = [
    path("create", BudgetCategoryCreateView.as_view(), name="budget-category-create"),
    path("list", BudgetCategoryListView.as_view(), name="budget-category-list"),
    path(
        "<int:pk>",
        BudgetCategoryRetrieveView.as_view(),
        name="budget-category-retrieve",
    ),
    path(
        "<int:pk>/update",
        BudgetCategoryUpdateView.as_view(),
        name="budget-category-update",
    ),
]
project_budget_patterns = [
    path("create", ProjectBudgetCreateView.as_view(), name="project-budget-create"),
    path("list", ProjectBudgetListView.as_view(), name="project-budget-list"),
    path(
        "<int:pk>", ProjectBudgetRetrieveView.as_view(), name="project-budget-retrieve"
    ),
    path(
        "<int:pk>/update",
        ProjectBudgetUpdateView.as_view(),
        name="project-budget-update",
    ),
]
project_patterns = [
    path("create", ProjectCreateView.as_view(), name="project-create"),
    path("list", ProjectListView.as_view(), name="project-list"),
    path("<int:pk>", ProjectRetrieveView.as_view(), name="project-retrieve"),
    path("<int:pk>/update", ProjectUpdateView.as_view(), name="project-update"),
]
task_patterns = [
    path("create", TaskCreateView.as_view(), name="task-create"),
    path("list", TaskListView.as_view(), name="task-list"),
    path("<int:pk>", TaskRetrieveView.as_view(), name="task-retrieve"),
    path("<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
]
urlpatterns = [
    path("companies/", include(company_patterns)),
    path("documents/", include(document_patterns)),
    path("milestones/", include(milestone_patterns)),
    path("budget-categories/", include(budget_category_patterns)),
    path("project-budgets/", include(project_budget_patterns)),
    path("projects/", include(project_patterns)),
    path("tasks/", include(task_patterns)),
]
