"""
Every upcoming apps' url will route through this urls.
On doing so, the API will be automatically documented
in swagger.
"""

from django.urls import include, path

urlpatterns = [
    path("auth-app/", include("apps.authentication.urls")),
    path("project-app/", include("apps.projects.urls")),
    path("material-app/", include("apps.materials.urls")),
    path("manpower-app/", include("apps.manpower.urls")),
    path("vendor-app/", include("apps.vendor.urls")),
]
