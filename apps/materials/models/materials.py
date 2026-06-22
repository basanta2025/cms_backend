from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from base.models import AbstractBaseModel, models


class MaterialType(AbstractBaseModel):
    name = models.CharField(max_length=20, default="", unique=True)
    is_active = models.BooleanField(default=True, help_text="Default to True")


class MaterialBrand(AbstractBaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)


class MaterialColour(AbstractBaseModel):
    name = models.CharField(max_length=20, default="", unique=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Default to True",
    )


class MaterialFlavour(AbstractBaseModel):
    name = models.CharField(max_length=20, default="", unique=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Default to True",
    )


class MaterialShape(AbstractBaseModel):
    name = models.CharField(max_length=20, default="", unique=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Default to True",
    )


class MaterialCompany(AbstractBaseModel):
    name = models.CharField(max_length=20, default="", unique=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Default to True",
    )


class MaterialGroup(AbstractBaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Category name can be max. of 100 characters",
    )
    code = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        help_text="Product code can be max. of 10 characters",
    )
    is_active = models.BooleanField(default=True, help_text="By default active=True")


class MaterialCategory(AbstractBaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "material_categories"
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class BaseUnit(MPTTModel, AbstractBaseModel):
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unit name can be max. of 50 characters and must be unique",
    )
    short_form = models.CharField(
        max_length=20,
        unique=True,
        help_text="short_form can be max. of 20 characters and must be unique",
    )
    display_order = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        help_text="Display order for ordering, default=0,blank= True, null= True",
    )
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="children"
    )

    is_active = models.BooleanField(default=True, help_text="By default active=True")

    @staticmethod
    def get_conversion_rate(self):
        conversion_rate = self.conversion_rate
        return float("{:.4f}".format(conversion_rate))

    def get_root_unit(self):
        """
        Instance method to fetch the root unit for the current instance.
        Traverses up the parent relationships to find the root unit.
        """
        unit_instance = self
        while unit_instance.parent:
            unit_instance = unit_instance.parent
        return unit_instance

    def get_units(self):
        """
        Instance method to fetch all units recursively for the current unit.
        """
        units = self.children.all()
        for unit in units:
            units |= unit.get_units()  # Recursively fetch all children
        return units

    def get_full_unit_hierarchy(self):
        """
        Instance method to fetch the full hierarchy from the root unit to the current unit.
        """
        hierarchy = []
        unit = self
        while unit:
            hierarchy.insert(0, unit)  # Insert at the beginning to reverse the order
            unit = unit.parent
        return hierarchy

    def __str__(self):
        return f"({self.pk}) - {self.name} ({self.short_form}) | {self.parent}"


class UnitConversion(AbstractBaseModel):
    from_unit = models.ForeignKey(
        BaseUnit, related_name="conversions_from", on_delete=models.CASCADE
    )
    to_unit = models.ForeignKey(
        BaseUnit, related_name="conversions_to", on_delete=models.CASCADE
    )
    conversion_rate = models.DecimalField(
        max_digits=settings.MAX_DECIMAL_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )

    def _validate_unique_together(self):
        if UnitConversion.objects.filter(
            from_unit=self.to_unit, to_unit=self.from_unit
        ).exists():
            self.errors_ = {
                "from_unit": [
                    "The reverse combination of 'to_unit' and 'from_unit' already exists."
                ],
                "to_unit": [
                    "The reverse combination of 'to_unit' and 'from_unit' already exists."
                ],
            }
            self.message_ = {
                "message": "The reverse combination of 'to_unit' and 'from_unit' already exists.",
            }
            self.raise_exception(self.errors_, self.message_)
        return super()._validate_unique_together()

    class Meta:
        unique_together = [
            ("from_unit", "to_unit"),
        ]

    def __str__(self):
        return f"({self.pk}) - [({self.from_unit.short_form}-{self.from_unit.pk})-({self.to_unit.short_form}-{self.to_unit.pk})]"


class Material(AbstractBaseModel):
    # company = models.ForeignKey(
    #     "projects.Company", on_delete=models.CASCADE, related_name="company_materials"
    # )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        "materials.MaterialCategory",
        on_delete=models.PROTECT,
        related_name="category_materials",
    )
    unit = models.CharField(max_length=50)  # e.g. kg, bags, pcs, m3
    unit_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
