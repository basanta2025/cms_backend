from django_filters import rest_framework as filters

from ..models import BaseUnit


class BaseUnitFilter(filters.FilterSet):
    parent_name = filters.CharFilter(field_name="parent__name", lookup_expr="icontains")

    class Meta:
        model = BaseUnit
        fields = {
            "parent": ["exact"],
            "is_active": ["exact"],
        }
