from base.models import AbstractBaseModel, models


class ProjectMaterial(AbstractBaseModel):
    project = models.ForeignKey(
        "projects.Project", on_delete=models.PROTECT, related_name="project_materials"
    )
    material = models.ForeignKey(
        "materials.Material", on_delete=models.PROTECT, related_name="project_materials"
    )
    qty_required = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    qty_ordered = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    qty_received = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    qty_used = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    notes = models.TextField(blank=True)
