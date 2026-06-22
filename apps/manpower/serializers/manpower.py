from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import AssignmentStatus, ManpowerAssignment


class ManpowerAssignmentCreateSerializer(BaseModelSerializer):
    class Meta:
        model = ManpowerAssignment
        exclude = ExcludeFields.exclude


class ManpowerAssignmentListSerializer(BaseModelSerializer):
    class Meta:
        model = ManpowerAssignment
        exclude = ExcludeFields.exclude


class ManpowerAssignmentRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = ManpowerAssignment
        exclude = ExcludeFields.exclude


class ManpowerAssignmentUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = ManpowerAssignment
        exclude = ExcludeFields.exclude
