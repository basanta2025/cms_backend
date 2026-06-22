from base.models import AbstractBaseModel, models


class AttendanceStatus(models.TextChoices):
    PRESENT = "present", "Present"
    ABSENT = "absent", "Absent"
    # HALF_DAY = "half_day", "Half-Day"
    LEAVE = "leave", "Leave"
    HOLIDAY = "holiday", "Holiday"


class AttendanceLog(AbstractBaseModel):
    worker = models.ForeignKey(
        "manpower.Worker", on_delete=models.CASCADE, related_name="worker_attendance"
    )
    marked_by = models.ForeignKey(
        "authentication.CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        related_name="marked_attendances",
    )
    work_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=AttendanceStatus.choices,
        default=AttendanceStatus.PRESENT,
    )
    hours_worked = models.DecimalField(max_digits=4, decimal_places=1, default=8.0)
    overtime_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)

    entry_time = models.TimeField(blank=True, null=True)
    extra_break_duration = models.DurationField(blank=True, null=True)
    leave_time = models.TimeField(blank=True, null=True)
    notes = models.TextField(blank=True)

    # project = models.ForeignKey(
    #     "projects.Project", on_delete=models.CASCADE, related_name="task_attendance"
    # )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "worker",
                    "work_date",
                ],
                name="unique_worker_daily_attendance",
            )
        ]
