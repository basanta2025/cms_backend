from django.core.validators import MaxValueValidator, MinValueValidator

from base.models import AbstractBaseModel, models


class TaskStatus(models.TextChoices):
    NOT_STARTED = "not_started", "Not Started"
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETED = "completed", "Completed"
    ON_HOLD = "on_hold", "On Hold"


class Task(AbstractBaseModel):
    milestone = models.ForeignKey(
        "projects.Milestone", on_delete=models.CASCADE, related_name="milestone_tasks"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=TaskStatus.choices, default=TaskStatus.NOT_STARTED
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    # Financial progress
    budget_allocated = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    budget_spent = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    financial_progress_pct = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    # Quantity progress (BOQ)
    unit_of_measure = models.CharField(max_length=50, blank=True)
    qty_planned = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    qty_completed = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    qty_progress_pct = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    # Manpower
    manpower_planned = models.PositiveIntegerField(default=0)
    manpower_deployed = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "tasks"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.milestone.title} — {self.title}"

    def save(self, *args, **kwargs):
        # Auto-calculate qty progress
        if self.qty_planned > 0:
            self.qty_progress_pct = (self.qty_completed / self.qty_planned) * 100
        # Auto-calculate financial progress
        if self.budget_allocated > 0:
            self.financial_progress_pct = (
                self.budget_spent / self.budget_allocated
            ) * 100
        super().save(*args, **kwargs)


# ─────────────────────────────────────────────
#  TASK PROGRESS LOG
# ─────────────────────────────────────────────


class TaskProgressLog(AbstractBaseModel):
    task = models.ForeignKey(
        "projects.Task", on_delete=models.CASCADE, related_name="task_progress"
    )
    logged_by = models.ForeignKey(
        "authentication.CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_task_logs",
    )
    log_date = models.DateField()
    financial_pct = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    qty_pct = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    qty_completed_today = models.DecimalField(
        max_digits=12, decimal_places=3, default=0
    )
    manpower_count = models.PositiveIntegerField(default=0)
    amount_spent_today = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    weather_condition = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "task_progress_logs"
        ordering = ["-log_date"]

    def __str__(self):
        return f"{self.task.title} — {self.log_date}"
