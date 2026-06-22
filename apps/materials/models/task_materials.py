from base.models import AbstractBaseModel, models


class TaskMaterial(AbstractBaseModel):
    task = models.ForeignKey(
        "projects.Task", on_delete=models.PROTECT, related_name="task_materials"
    )
    material = models.ForeignKey(
        "materials.Material", on_delete=models.PROTECT, related_name="task_materials"
    )
    qty_required = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    qty_used = models.DecimalField(max_digits=12, decimal_places=3, default=0)
