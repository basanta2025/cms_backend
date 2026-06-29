from django.core.validators import MaxValueValidator, MinValueValidator

from base.models import AbstractBaseModel, models


class PaymentStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    VERIFIED = "verified", "Verified"
    PAID = "paid", "Paid"
    CANCELLED = "cancelled", "Cancelled"
    PARTIAL = "partial", "Partial"


class SalarySheet(AbstractBaseModel):
    worker = models.ForeignKey(
        "manpower.Worker", on_delete=models.CASCADE, related_name="worker_salary_sheets"
    )
    # project = models.ForeignKey(
    #     "projects.Project",

    #     on_delete=models.CASCADE,
    #     related_name="project_salary_sheets",
    # )
    generated_by = models.ForeignKey(
        "authentication.CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="generated_salaries",
    )
    month = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    year = models.PositiveIntegerField()

    # Attendance summary
    days_present = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    days_absent = models.PositiveIntegerField(default=0)
    total_overtime_hours = models.DecimalField(
        max_digits=6, decimal_places=1, default=0
    )

    # Earnings
    basic_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    overtime_pay = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    allowances = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bonus = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    # Deductions
    advance_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_deductions = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    # Net
    gross_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    paid_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    payment_status = models.CharField(
        max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.DRAFT
    )
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["worker", "project", "month", "year"],
                name="unique_salary_per_worker_project_month_year",
            )
        ]
