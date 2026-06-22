from base.models import AbstractBaseModel, models


class Company(AbstractBaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    logo_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
