from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import Material, MaterialCategory
from ..serializers import (
    MaterialCategoryCreateSerializer,
    MaterialCategoryListSerializer,
    MaterialCategoryRetrieveSerializer,
    MaterialCategoryUpdateSerializer,
    MaterialCreateSerializer,
    MaterialListSerializer,
    MaterialRetrieveSerializer,
    MaterialUpdateSerializer,
)


# ----------Material Category
class MaterialCategoryCreateView(CustomGenericCreateView):
    serializer_class = MaterialCategoryCreateSerializer
    queryset = MaterialCategory.objects.all()
    success_response_message = "Material Category Created Successfully"


class MaterialCategoryListView(CustomGenericListView):
    serializer_class = MaterialCategoryListSerializer
    queryset = MaterialCategory.objects.all()
    success_response_message = "Material Category Fetched Successfully"


class MaterialCategoryRetrieveView(CustomGenericRetrieveView):
    serializer_class = MaterialCategoryRetrieveSerializer
    queryset = MaterialCategory.objects.all()
    success_response_message = "Material Category Retrieved Successfully"


class MaterialCategoryUpdateView(CustomGenericUpdateView):
    serializer_class = MaterialCategoryUpdateSerializer
    queryset = MaterialCategory.objects.all()
    success_response_message = "Material Category Updated Successfully"


# -------Material


class MaterialCreateView(CustomGenericCreateView):
    serializer_class = MaterialCreateSerializer
    queryset = Material.objects.all()
    success_response_message = "Material Created Successfully"


class MaterialListView(CustomGenericListView):
    serializer_class = MaterialListSerializer
    queryset = Material.objects.all()
    success_response_message = "Material Fetched Successfully"


class MaterialRetrieveView(CustomGenericRetrieveView):
    serializer_class = MaterialRetrieveSerializer
    queryset = Material.objects.all()
    success_response_message = "Material Retrieved Successfully"


class MaterialUpdateView(CustomGenericUpdateView):
    serializer_class = MaterialUpdateSerializer
    queryset = Material.objects.all()
    success_response_message = "Material Updated Successfully"
