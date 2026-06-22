from base.models import AbstractBaseModel, models


class EntryType(models.TextChoices):
    DEBIT = "debit", "Debit"
    CREDIT = "credit", "Credit"


class Accounts(AbstractBaseModel):
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="trial_balance_entries",
    )
    account_code = models.CharField(max_length=20)
    account_name = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=10, choices=EntryType.choices)
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    entry_date = models.DateField()
    reference_no = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
