from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from base.models import AbstractBaseModel


class VATTreatmentChoices(models.TextChoices):
    REGISTERED = "Registered", "Registered Business - Regular"
    COMPOSITION = "Composition", "Registered Business - Composition"
    UNREGISTERED = "Unregistered", "Unregistered Business"
    CONSUMER = "Consumer", "Consumer"
    OVERSEAS = "Overseas", "Overseas"
    SPECIAL = "Special", "Special Economic Zone"


class VendorLabourType(AbstractBaseModel):
    """
    Multiple labour types per vendor.
    e.g. Electrician, Plumber, Carpenter
    """

    # Validate to ensure that this is only created for vendors of type LABOUR
    vendor = models.ForeignKey(
        "vendor.Vendor",
        on_delete=models.CASCADE,
        related_name="labour_types",
    )
    name = models.CharField(max_length=100)


# class VendorWorker(AbstractBaseModel):
#     """
#     Stores individual named workers under a vendor.
#     Used when attendance_method == "Each Worker Separately"
#     """

#     vendor = models.ForeignKey(
#         Vendor,
#         on_delete=models.CASCADE,
#         related_name="workers",
#     )
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)


class VendorContactPerson(AbstractBaseModel):
    """
    Multiple contact persons per vendor.
    """

    vendor = models.ForeignKey(
        "vendor.Vendor",
        on_delete=models.CASCADE,
        related_name="contact_persons",
    )
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    business_address = models.TextField(blank=True)


class VendorFinancialDetail(AbstractBaseModel):
    """
    One-to-one financial and address details for a vendor.
    """

    vendor = models.OneToOneField(
        "vendor.Vendor",
        on_delete=models.CASCADE,
        related_name="financial_detail",
    )
    business_address = models.TextField(blank=True)
    vat_treatment = models.CharField(
        max_length=100,
        choices=VATTreatmentChoices.choices,
        blank=True,
    )
    pan_number = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )
    vat_number = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )
    terms_and_conditions = models.TextField(blank=True)


class VendorPaymentTerm(AbstractBaseModel):
    """
    Multiple payment terms per vendor.
    e.g. Net 30, Net 60
    """

    vendor = models.ForeignKey(
        "vendor.Vendor",
        on_delete=models.CASCADE,
        related_name="payment_terms",
    )
    term_name = models.CharField(max_length=100)
    no_of_days = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
    )


class VendorBankAccount(AbstractBaseModel):
    """
    Multiple bank accounts per vendor.
    """

    vendor = models.ForeignKey(
        "vendor.Vendor",
        on_delete=models.CASCADE,
        related_name="bank_accounts",
    )
    bank_name = models.CharField(max_length=255)
    account_holder_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)


class VendorDocument(AbstractBaseModel):
    """
    Supporting documents uploaded for a vendor.
    Limit: 10 files — enforced at serializer level.
    """

    vendor = models.ForeignKey(
        "vendor.Vendor",
        on_delete=models.CASCADE,
        related_name="documents",
    )
    file = models.FileField(upload_to="vendor_documents/%Y/%m/")
    file_name = models.CharField(
        max_length=255,
        blank=True,
        help_text="Original filename for display purposes.",
    )
