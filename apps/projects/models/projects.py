from django.core.validators import MaxValueValidator, MinValueValidator

from base.models import AbstractBaseModel, models


class ProjectStatus(models.TextChoices):
    PLANNING = "planning", "Planning"
    ACTIVE = "active", "Active"
    ON_HOLD = "on_hold", "On Hold"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"


class Project(AbstractBaseModel):
    company = models.ForeignKey(
        "projects.Company", on_delete=models.CASCADE, related_name="company_projects"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    client_name = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=20, choices=ProjectStatus.choices, default=ProjectStatus.PLANNING
    )
    start_date = models.DateField()
    end_date = models.DateField()
    contract_value = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_budget = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    progress_pct = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
