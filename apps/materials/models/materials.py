from django.conf import settings

from base.models import AbstractBaseModel, models


class MaterialCategory(AbstractBaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "material_categories"
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class Material(AbstractBaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        "materials.MaterialCategory",
        on_delete=models.PROTECT,
        related_name="category_materials",
    )
    material_type = models.ForeignKey(
        "materials.MaterialType",
        on_delete=models.PROTECT,
        related_name="material_type",
    )
    base_unit = models.ForeignKey(
        "materials.BaseUnit",
        on_delete=models.PROTECT,
        help_text="Base Unit Id of the product.",
        related_name="base_unit_materials",
    )
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    # group
