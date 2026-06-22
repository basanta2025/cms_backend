from base.models import AbstractBaseModel, models


class BudgetCategory(AbstractBaseModel):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)


class ProjectBudget(AbstractBaseModel):
    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="project_budgets"
    )
    cost_head = models.CharField(max_length=255)
    category = models.ForeignKey(
        BudgetCategory,
        on_delete=models.CASCADE,
        related_name="project_budgets_category",
    )
    estimated_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    actual_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
