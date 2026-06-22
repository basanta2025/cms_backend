from django.core.validators import MaxValueValidator, MinValueValidator

from base.models import AbstractBaseModel, models


class MilestoneStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETED = "completed", "Completed"
    DELAYED = "delayed", "Delayed"


class Milestone(AbstractBaseModel):
    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="milestones"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    sequence_no = models.PositiveIntegerField(default=1)
    start_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=20, choices=MilestoneStatus.choices, default=MilestoneStatus.PENDING
    )
    progress_pct = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    budget_allocated = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    payment_linked = models.BooleanField(default=False)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
