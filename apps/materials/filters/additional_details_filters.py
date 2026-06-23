from django_filters import rest_framework as filters

from ..models import MaterialAdditionalDetails


class MaterialAdditionalDetailsFilter(filters.FilterSet):
    material_name = filters.CharFilter(
        field_name="material__name", lookup_expr="icontains"
    )
    brand_name = filters.CharFilter(field_name="brand__name", lookup_expr="icontains")
    colour_name = filters.CharFilter(field_name="colour__name", lookup_expr="icontains")

    shape_name = filters.CharFilter(field_name="shape__name", lookup_expr="icontains")
    company_name = filters.CharFilter(
        field_name="company_name__name", lookup_expr="icontains"
    )
    excise_unit_name = filters.CharFilter(
        field_name="excise_unit__name", lookup_expr="icontains"
    )
    purchase_unit_name = filters.CharFilter(
        field_name="purchase_unit__name", lookup_expr="icontains"
    )
    purchase_cost_unit_name = filters.CharFilter(
        field_name="purchase_cost_unit__name", lookup_expr="icontains"
    )
    sale_unit_name = filters.CharFilter(
        field_name="sale_unit__name", lookup_expr="icontains"
    )
    sale_cost_unit_name = filters.CharFilter(
        field_name="sale_cost_unit__name", lookup_expr="icontains"
    )

    class Meta:
        model = MaterialAdditionalDetails
        fields = {
            "material": ["exact"],
            "brand": ["exact"],
            "colour": ["exact"],
            "shape": ["exact"],
            "company": ["exact"],
            "excise_unit": ["exact"],
            "purchase_unit": ["exact"],
            "purchase_cost_unit": ["exact"],
            # "sale_unit": ["exact"],
            # "sale_cost_unit": ["exact"],
            # "for_branch": ["exact"],
        }
