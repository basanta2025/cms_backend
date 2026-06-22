from base.models import AbstractBaseModel, models


class OverTime(AbstractBaseModel):
    attendance_log = models.ForeignKey(
        "manpower.AttendanceLog", on_delete=models.PROTECT
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    overtime_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    description = models.TextField()
