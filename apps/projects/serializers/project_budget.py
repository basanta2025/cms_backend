from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import BudgetCategory, ProjectBudget


# --------------BudgetCategory------------------------
class BudgetCategoryCreateSerializer(BaseModelSerializer):
    class Meta:
        model = BudgetCategory
        exclude = ExcludeFields.exclude


class BudgetCategoryListSerializer(BaseModelSerializer):
    class Meta:
        model = BudgetCategory
        exclude = ExcludeFields.exclude


class BudgetCategoryRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = BudgetCategory
        exclude = ExcludeFields.exclude


class BudgetCategoryUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = BudgetCategory
        exclude = ExcludeFields.exclude


# --------------ProjectBudget------------------------
class ProjectBudgetCreateSerializer(BaseModelSerializer):
    class Meta:
        model = ProjectBudget
        exclude = ExcludeFields.exclude


class ProjectBudgetListSerializer(BaseModelSerializer):
    class Meta:
        model = ProjectBudget
        exclude = ExcludeFields.exclude


class ProjectBudgetRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = ProjectBudget
        exclude = ExcludeFields.exclude


class ProjectBudgetUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = ProjectBudget
        exclude = ExcludeFields.exclude
