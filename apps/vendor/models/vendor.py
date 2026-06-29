from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from base.models import AbstractBaseModel


class AttendanceMethodChoices(models.TextChoices):
    COUNT_OF_WORKERS = "Count of Workers", "Count of Workers"
    EACH_WORKER_SEPARATELY = "Each Worker Separately", "Each Worker Separately"


class VendorTypeChoices(models.TextChoices):
    LABOUR = "Labour", "Labour"
    MATERIAL = "Material", "Material"
    SUB_CONTRACTOR = "Sub-Contractor", "Sub-Contractor"


class Vendor(AbstractBaseModel):
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=100,
        choices=VendorTypeChoices.choices,
    )
    attendance_method = models.CharField(
        max_length=100,
        choices=AttendanceMethodChoices.choices,
        blank=True,
        null=True,
        help_text="Only applicable when vendor type is Labour.",
    )
    account_group = models.ForeignKey(
        "accounting.GLAccountGroup",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="vendors",
    )
    code = models.CharField(
        max_length=20,
        unique=True,
        help_text="Unique code for the vendor.",
    )
    salesman = models.CharField(
        max_length=255,
        default="",
        blank=True,
        help_text="Enter the name of the salesperson assigned to this party.",
    )
    notes = models.TextField(
        blank=True,
        default="",
        help_text="Any additional notes or remarks related to the party.",
    )
    is_active = models.BooleanField(default=True)
