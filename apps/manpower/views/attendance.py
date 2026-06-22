from base.serializers import BaseModelSerializer, ExcludeFields
from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import AttendanceLog, AttendanceStatus
from ..serializers import (
    AttendanceLogCreateSerializer,
    AttendanceLogListSerializer,
    AttendanceLogRetrieveSerializer,
    AttendanceLogUpdateSerializer,
)


class AttendanceLogCreateView(CustomGenericCreateView):
    serializer_class = AttendanceLogCreateSerializer
    queryset = AttendanceLog.objects.all()
    success_response_message = "Attendance Log Created Successfuly"


class AttendanceLogListView(CustomGenericListView):
    serializer_class = AttendanceLogListSerializer
    queryset = AttendanceLog.objects.all()
    success_response_message = "Attendance Log fetched Successfuly"


class AttendanceLogRetrieveView(CustomGenericRetrieveView):
    serializer_class = AttendanceLogRetrieveSerializer
    queryset = AttendanceLog.objects.all()
    success_response_message = "Attendance Log Retrieved Successfuly"


class AttendanceLogUpdateView(CustomGenericUpdateView):
    serializer_class = AttendanceLogUpdateSerializer
    queryset = AttendanceLog.objects.all()
    success_response_message = "Attendance Log Updated Successfuly"
