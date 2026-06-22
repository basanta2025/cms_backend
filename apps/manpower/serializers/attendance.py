from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import AttendanceLog, AttendanceStatus


class AttendanceLogCreateSerializer(BaseModelSerializer):
    class Meta:
        model = AttendanceLog
        exclude = ExcludeFields.exclude


class AttendanceLogListSerializer(BaseModelSerializer):
    class Meta:
        model = AttendanceLog
        exclude = ExcludeFields.exclude


class AttendanceLogRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = AttendanceLog
        exclude = ExcludeFields.exclude


class AttendanceLogUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = AttendanceLog
        exclude = ExcludeFields.exclude
