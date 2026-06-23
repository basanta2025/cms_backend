from django_filters import rest_framework as filters

from ..models import MaterialCategory


class MaterialCategoryFilter(filters.FilterSet):
    parent_name = filters.CharFilter(field_name="parent__name", lookup_expr="icontains")

    class Meta:
        model = MaterialCategory
        fields = {
            # "parent": ["exact"],
        }
