from base.models import AbstractBaseModel, models


class Document(AbstractBaseModel):
    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="project_documents"
    )
    # task = models.ForeignKey(
    #     "projects.Task",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="drawings",
    # )
    title = models.CharField(max_length=255)
    document_no = models.CharField(max_length=100, blank=True)
    # drawing_type = models.CharField(
    #     max_length=30, choices=DrawingType.choices, default=DrawingType.OTHER
    # )
    # revision = models.CharField(max_length=20, default="R0")
    image = models.ImageField(upload_to="project_documents/")
    description = models.TextField(blank=True)
    is_latest_revision = models.BooleanField(default=True)
