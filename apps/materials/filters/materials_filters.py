from django_filters import rest_framework as filters

from ..models import Material


class MaterialFilter(filters.FilterSet):
    category_name = filters.CharFilter(
        field_name="category__name", lookup_expr="icontains"
    )

    class Meta:
        model = Material
        # fields = {
        #     "pk": ["exact"],
        #     "group": ["exact"],
        #     "base_unit": ["exact"],
        #     "category": ["exact"],
        #     "product_type": ["exact"],
        # }

        fields = [
            "id",
            "name",
            # "group",
            "base_unit",
            "category",
            "material_type",
            "category_name",
        ]
