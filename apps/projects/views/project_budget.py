from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import ProjectBudget
from ..serializers import (
    BudgetCategoryCreateSerializer,
    BudgetCategoryListSerializer,
    BudgetCategoryRetrieveSerializer,
    BudgetCategoryUpdateSerializer,
    ProjectBudgetCreateSerializer,
    ProjectBudgetListSerializer,
    ProjectBudgetRetrieveSerializer,
    ProjectBudgetUpdateSerializer,
)

# -------------Budget Category Views-----------------#


class BudgetCategoryCreateView(CustomGenericCreateView):
    queryset = ProjectBudget.objects.all()
    serializer_class = BudgetCategoryCreateSerializer
    success_message = "Budget category created successfully."


class BudgetCategoryListView(CustomGenericListView):
    queryset = ProjectBudget.objects.all()
    serializer_class = BudgetCategoryListSerializer
    success_message = "Budget categories fetched successfully."


class BudgetCategoryRetrieveView(CustomGenericRetrieveView):
    queryset = ProjectBudget.objects.all()
    serializer_class = BudgetCategoryRetrieveSerializer
    success_message = "Budget category retrieved successfully."


class BudgetCategoryUpdateView(CustomGenericUpdateView):
    queryset = ProjectBudget.objects.all()
    serializer_class = BudgetCategoryUpdateSerializer
    success_message = "Budget category updated successfully."


# ----------------Project Budget Views-----------------#


class ProjectBudgetCreateView(CustomGenericCreateView):
    queryset = ProjectBudget.objects.all()
    serializer_class = ProjectBudgetCreateSerializer
    success_message = "Project budget created successfully."


class ProjectBudgetListView(CustomGenericListView):
    queryset = ProjectBudget.objects.all()
    serializer_class = ProjectBudgetListSerializer
    success_message = "Project budgets fetched successfully."


class ProjectBudgetRetrieveView(CustomGenericRetrieveView):
    queryset = ProjectBudget.objects.all()
    serializer_class = ProjectBudgetRetrieveSerializer
    success_message = "Project budget retrieved successfully."


class ProjectBudgetUpdateView(CustomGenericUpdateView):
    queryset = ProjectBudget.objects.all()
    serializer_class = ProjectBudgetUpdateSerializer
    success_message = "Project budget updated successfully."
