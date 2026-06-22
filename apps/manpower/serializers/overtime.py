from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import OverTime


class OverTimeCreateSerializer(BaseModelSerializer):
    class Meta:
        model = OverTime
        exclude = ExcludeFields.exclude


class OverTimeListSerializer(BaseModelSerializer):
    class Meta:
        model = OverTime
        exclude = ExcludeFields.exclude


class OverTimeRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = OverTime
        exclude = ExcludeFields.exclude


class OverTimeUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = OverTime
        exclude = ExcludeFields.exclude
