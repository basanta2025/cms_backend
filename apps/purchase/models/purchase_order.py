import datetime

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import transaction
from django.utils import timezone

from base.models import AbstractBaseModel, models


class PurchaseOrderMain(AbstractBaseModel):
    order_no = models.CharField(
        max_length=50,
        unique=True,
        help_text="Order no. should be max. of 50 characters",
    )
    # PurchaseOrderFromBranch - PurchaseOrderMain should be 1-1
    # We can't give access to create the PO multiple times
    # for the branch purchase order from indent request (PurchaseOrderFromBranch)

    purchase_date = models.DateField(
        default=datetime.date.today,
        help_text="Purchase Date",
    )
    serial_number = models.CharField(
        max_length=50,
        # unique=True,
        blank=True,
        default="",
        help_text="Serial no. should be max. of 50 characters",
    )
    narration = models.TextField(
        blank=True,
        default="",
        help_text="Narration",
    )
    discount_amount = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default="0.00",
        help_text="Discount Amount.",
        validators=[
            MinValueValidator(0),
        ],
    )
    vendor_account = models.ForeignKey(
        "vendor.Vendor",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="purchase_order_vendor_account",
    )

    grand_total = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        help_text="Grand Total Amount.",
        validators=[
            MinValueValidator(0),
        ],
        default="0.00",
    )
    vat_amount = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        help_text="VAT Amount.",
        validators=[
            MinValueValidator(0),
        ],
        default="0.00",
    )
    voucher_date = models.DateField(default=datetime.date.today)
    voucher_date_bs = models.CharField(
        default="", blank=True, max_length=15, help_text="Voucher Date in BS"
    )


class PurchaseDetailStatus(models.TextChoices):
    OPEN = "open", "Open"
    CLOSED = "closed", "Closed"


class PurchaseOrderDetail(AbstractBaseModel):
    purchase_order_main = models.ForeignKey(
        PurchaseOrderMain,
        on_delete=models.PROTECT,
        related_name="purchase_order_details",
    )
    # status =
    actual_quantity = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        help_text="Actual Quantity of the Product.",
    )

    unit = models.ForeignKey(
        "products.BaseUnit",
        related_name="purchase_base_units",
        on_delete=models.PROTECT,
        help_text="Base Unit Id",
    )
    product = models.ForeignKey(
        "products.Product",
        related_name="purchase_order_products",
        on_delete=models.PROTECT,
        help_text="Product Id",
    )
    rate = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        validators=[MinValueValidator(0)],
        help_text="Rate.",
    )
    amount = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        validators=[MinValueValidator(0)],
        help_text="Amount.",
    )

    alt_unit = models.ForeignKey(
        "products.BaseUnit",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="alt_purchase_order_detail",
    )
    alt_quantity = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default=0.0,
        validators=[
            MinValueValidator(0),
        ],
    )
    closed_quantity = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default=0.0,
        editable=False,
        validators=[
            MinValueValidator(0),
        ],
    )
    status = models.CharField(
        max_length=10,
        choices=PurchaseDetailStatus.choices,
        default=PurchaseDetailStatus.OPEN,
        editable=False,
    )
