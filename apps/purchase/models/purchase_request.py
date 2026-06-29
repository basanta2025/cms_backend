from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import transaction
from django.utils import timezone

from base.models import AbstractBaseModel, models


class PurchaseOrderRequest(AbstractBaseModel):
    # Master
    indent_no = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique indent number for the tracking",
    )

    # request_branch = Here we are treating the 'branch' field from BranchModelMixin as Request Branch
    # Can be null, because the user can also request directly from head office
    # Check is_from_ho field.
    receiver_project = models.ForeignKey(
        "projects.Project",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="receiver_project",
        help_text="To which project the indent should be requested.",
    )
    required_date_ad = models.DateField(
        help_text="Required Date in AD",
    )
    required_date_bs = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        editable=False,
        help_text="Required Date in BS",
    )
    voucher_date = models.DateField(
        help_text="Voucher Date in AD",
    )
    voucher_date_bs = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        editable=False,
        help_text="Voucher Date in BS",
    )
    narration = models.TextField(default="", help_text="Narration for the indent.")

    requester_name = models.ForeignKey(
        "authentication.CustomUser",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        help_text="The name of the requester.",
    )

    department = models.ForeignKey(
        "departments.Department",
        blank=True,
        null=True,
        related_name="purchase_order_request_departments",
        on_delete=models.PROTECT,
        help_text="For which department?",
    )
    # By default False -> POR receiver branch head_office
    place_of_supply = models.CharField(blank=True, null=True, default="")

    vendor_account = models.ForeignKey(
        "vendor.Vendor",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="purchase_request_vendor_account",
    )

    grand_total = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default="0.00",
        help_text="Grand Total Amount.",
        validators=[MinValueValidator(0)],
    )
    vat_amount = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default="0.00",
        help_text="VAT Amount.",
        validators=[MinValueValidator(0)],
    )


class PurchaseOrderRequestDetail(AbstractBaseModel):
    purchase_order_request = models.ForeignKey(
        PurchaseOrderRequest,
        on_delete=models.PROTECT,
        related_name="purchase_order_request_details",
        help_text="Id of PurchaseOrderRequest Master",
    )

    material = models.ForeignKey(
        "materials.Material",
        related_name="purchase_request_materials",
        on_delete=models.PROTECT,
        help_text="Material Id",
    )

    closing_stock = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        help_text="Closing Stock Value.",
        validators=[MinValueValidator(0)],
    )

    description = models.CharField(
        max_length=150,
        null=True,
        help_text="Description for the material request detail.",
    )
    actual_quantity = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        validators=[MinValueValidator(0)],
        help_text="Actual Quantity of the Material.",
    )

    unit = models.ForeignKey(
        "products.BaseUnit",
        related_name="purchase_request_base_units",
        on_delete=models.PROTECT,
        help_text="Base Unit Id",
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
        help_text="Amount",
    )
    required_date = models.DateField(
        default=timezone.now,
        help_text="Date field for the material Required Date. Should not be less than today.",
    )
