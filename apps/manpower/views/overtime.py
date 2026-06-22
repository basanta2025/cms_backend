from base.serializers import BaseModelSerializer, ExcludeFields
from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import OverTime
from ..serializers import (
    OverTimeCreateSerializer,
    OverTimeListSerializer,
    OverTimeRetrieveSerializer,
    OverTimeUpdateSerializer,
)


class OverTimeCreateView(CustomGenericCreateView):
    serializer_class = OverTimeCreateSerializer
    queryset = OverTime.objects.all()
    success_response_message = "OverTime Created Successfully"


class OverTimeListView(CustomGenericListView):
    serializer_class = OverTimeListSerializer
    queryset = OverTime.objects.all()
    success_response_message = "OverTime Fetched Successfully"


class OverTimeRetrieveView(CustomGenericRetrieveView):
    serializer_class = OverTimeRetrieveSerializer
    queryset = OverTime.objects.all()
    success_response_message = "OverTime Retrieved Successfully"


class OverTimeUpdateView(CustomGenericUpdateView):
    serializer_class = OverTimeUpdateSerializer
    queryset = OverTime.objects.all()
    success_response_message = "OverTime Updated Successfully"
