from base.models import AbstractBaseModel, models


class AssignmentStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    COMPLETED = "completed", "Completed"
    TRANSFERRED = "transferred", "Transferred"
    INCOMPLETE = "incomplete", "Incomplete"


class ManpowerAssignment(AbstractBaseModel):
    task = models.ForeignKey(
        "projects.Task",
        on_delete=models.CASCADE,
        related_name="manpower_assignments",
    )
    worker = models.ForeignKey(
        "manpower.Worker", on_delete=models.CASCADE, related_name="assignments"
    )
    assigned_from = models.DateField()
    assigned_to = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=AssignmentStatus.choices, default=AssignmentStatus.ACTIVE
    )
    notes = models.TextField(blank=True)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=["worker", "task"],
    #             name="unique_worker_task",
    #         )
    #     ]
