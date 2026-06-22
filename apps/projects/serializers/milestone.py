from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import Milestone


class MilestoneCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Milestone
        exclude = ExcludeFields.exclude


class MilestoneListSerializer(BaseModelSerializer):
    class Meta:
        model = Milestone
        exclude = ExcludeFields.exclude


class MilestoneRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = Milestone
        exclude = ExcludeFields.exclude


class MilestoneUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = Milestone
        exclude = ExcludeFields.exclude
