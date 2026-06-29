from decimal import Decimal

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from base.models import AbstractBaseModel, models

User = get_user_model()


class AccountType(models.TextChoices):
    ASSET = "asset", "Asset"
    LIABILITY = "liability", "Liability"
    INCOME = "income", "Income"
    EXPENSE = "expense", "Expense"
    EQUITY = "equity", "Equity"


class GLAccountGroup(AbstractBaseModel, MPTTModel):
    ACCOUNT_TYPES = (
        ("asset", "Asset"),
        ("liability", "Liability"),
        ("income", "Income"),
        ("expense", "Expense"),
        ("equity", "Equity"),
    )

    name = models.CharField(max_length=250, unique=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        help_text="Parent GL Account Group",
    )
    account_type = models.CharField(
        max_length=20,
        choices=AccountType.choices,
        help_text="Type of account group for reporting (BS/PL).",
    )
    is_active = models.BooleanField(default=True)
    remarks = models.TextField(null=True, blank=True)

    is_control_account = models.BooleanField(
        default=False,
        help_text="Is this account a control account?",
    )

    def __str__(self):
        return f"({self.pk})-{self.name}"

    @property
    def get_groups(self):
        return self.get_descendants().values_list("id", "name")

    @property
    def get_group_list(self):
        return self.get_descendants().values_list("name")

    def _validate_control_account(self):
        if not self.is_control_account:
            return

        if self.parent and self.parent.is_control_account:
            error = {
                "parent": ["Control account can not refer to another control account."],
            }
            message = {
                "message": "Control account can not refer to another control account.",
            }
            self.raise_exception(errors=error, message=message)

    def _validate_required_field(self) -> None:
        self._validate_control_account()
        return super()._validate_required_field()

    def save(self, *args, **kwargs):
        if self.pk and self.parent:
            if self.pk == self.parent.id:
                message = {
                    "message": "A node may not be made a child of itself.",
                }
                errors = {
                    "parent": [
                        "A node may not be made a child of itself.",
                    ],
                }
                self.raise_exception(errors=errors, message=message)
        return super().save(*args, **kwargs)


class GLAccount(MPTTModel, AbstractBaseModel):
    """
    Represents a postable ledger account.

    - Control accounts (non-postable) should be marked and must be standalone.
    - Postable accounts should be assigned to non-control groups.
    """

    name = models.CharField(max_length=250)
    code = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        default="",
        help_text="Unique ledger code.",
    )
    account_group = models.ForeignKey(
        GLAccountGroup,
        on_delete=models.CASCADE,
        related_name="accounts",
        help_text="GLAccountGroup ID.",
    )
    reference_number = models.CharField(
        default="",
        max_length=100,
        help_text="Reference to entity in the system.",
    )
    opening_balance = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default=Decimal("0.00"),
    )

    postings_allowed = models.BooleanField(
        default=True,
        help_text="If false, posting to this account is restricted",
    )
    vendor_account = models.OneToOneField(
        "vendor.Vendor",
        on_delete=models.PROTECT,
        related_name="gl_account",
        null=True,
        blank=True,
    )
    # additional_charges = models.OneToOneField(
    #     "core_app.AdditionalCharge",
    #     on_delete=models.PROTECT,
    #     related_name="gl_account",
    #     null=True,
    #     blank=True,
    # )
    # grn_additional_invoice_cost = models.OneToOneField(
    #     "purchase.GrnAdditionalInvoiceCost",
    #     on_delete=models.PROTECT,
    #     related_name="gl_account",
    #     null=True,
    #     blank=True,
    # )
    material_group = models.OneToOneField(
        "materials.MaterialGroup",
        on_delete=models.PROTECT,
        related_name="gl_account",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_system_generated = models.BooleanField(default=False, editable=False)
    merged = models.BooleanField(default=False)
    merged_to = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text="If merged, this account's data refers to another account.",
    )
    is_cash_account = models.BooleanField(
        default=False,
        help_text="Is this account a cash account?",
    )
    remarks = models.TextField(
        default="", blank=True, help_text="Remarks of the account."
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name="children",
        help_text="Parent should be control account.",
    )
    # currency = models.CharField(
    #     max_length=10, default="NPR", help_text="Currency of the account"
    # )
    # tax_category = models.CharField(
    #     max_length=20, blank=True, null=True, help_text="E.g., VAT, TDS"
    # )

    # def _validate_control_and_party_account(self):
    #     self.parent = self.control_account

    #     control_cash_account = [self.is_control_account, self.is_cash_account]

    #     if all(control_cash_account):
    #         errors = {
    #             "is_control_account": [
    #                 "Account can not be both control and cash account."
    #             ],
    #             "is_cash_account": [
    #                 "Account can not be both control and cash account."
    #             ],
    #         }
    #         message = {
    #             "message": "Account can not be both control and cash account.",
    #         }

    #         self.raise_exception(errors=errors, message=message)

    #     is_control_and_ref_to_control_account = [
    #         self.is_control_account,
    #         True if self.control_account else False,
    #     ]

    #     if all(is_control_and_ref_to_control_account):
    #         errors = {
    #             "is_control_account": [
    #                 "Control account can not refer to another control account."
    #             ],
    #             "control_account": [
    #                 "Control account can not refer to another control account."
    #             ],
    #         }
    #         message = {
    #             "message": "Control account can not refer to another control account.",
    #         }
    #         self.raise_exception(errors=errors, message=message)

    #     if self.control_account:
    #         # Means this is not a control account
    #         # If it is a control account then there is a boolean field to indicate that.
    #         # So we need to populate the account group from the control account
    #         if not self.control_account.is_control_account:
    #             self.raise_exception(
    #                 errors={
    #                     "control_account": ["This is not a control account."],
    #                 },
    #                 message={
    #                     "message": "Invalid control account provided.",
    #                 },
    #             )
    #         self.account_group = self.control_account.account_group
    #     if not self.account_group:
    #         self.raise_exception(
    #             errors={
    #                 "control_account": [
    #                     "No account group found associated to this control account."
    #                 ],
    #             },
    #             message={
    #                 "message": "No account group found associated to this control account.",
    #             },
    #         )

    # def _validate_required_field(self) -> None:
    #     self._validate_control_and_party_account()
    #     return super()._validate_required_field()

    # def __str__(self) -> str:
    #        return f"({self.pk})-{self.name}"

    def save(self, *args, **kwargs):
        if not self.code:
            import uuid

            self.code = uuid.uuid4()

        self.reference_number = self.code
        return super().save(*args, **kwargs)
