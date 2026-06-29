from base.models import AbstractBaseModel, models


class PayType(models.TextChoices):
    DAILY = "daily", "Daily"
    MONTHLY = "monthly", "Monthly"
    HOURLY = "hourly", "Hourly"


class WorkerCategory(AbstractBaseModel):
    name = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=5, unique=True)
    description = models.TextField()


class Worker(AbstractBaseModel):
    vendor = models.ForeignKey(
        "vendor.Vendor",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="workers",
        help_text="The vendor this worker belongs to. Null if independent worker.",
    )
    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        WorkerCategory,
        on_delete=models.PROTECT,
        related_name="workers",
    )
    pay_type = models.CharField(
        max_length=10, choices=PayType.choices, default=PayType.DAILY
    )
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monthly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    overtime_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    bank_account = models.CharField(max_length=50, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)


# def worker_document_path(instance, filename):
#     return f"workers/{instance.worker_id}/documents/{filename}"


class WorkerDocument(AbstractBaseModel):
    worker = models.ForeignKey(
        "manpower.Worker", on_delete=models.CASCADE, related_name="doc_images"
    )
    document_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="worker_documents/")
    document_no = models.CharField(max_length=15, blank=True, null=True)
