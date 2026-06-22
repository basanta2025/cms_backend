from base.serializers import BaseModelSerializer, ExcludeFields
from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import AssignmentStatus, ManpowerAssignment
from ..serializers import (
    ManpowerAssignmentCreateSerializer,
    ManpowerAssignmentListSerializer,
    ManpowerAssignmentRetrieveSerializer,
    ManpowerAssignmentUpdateSerializer,
)


class ManpowerAssignmentCreateView(CustomGenericCreateView):
    serializer_class = ManpowerAssignmentCreateSerializer
    queryset = ManpowerAssignment.objects.all()
    success_response_message = "Manpower Assigned Successfully"


class ManpowerAssignmentListView(CustomGenericListView):
    serializer_class = ManpowerAssignmentListSerializer
    queryset = ManpowerAssignment.objects.all()
    success_response_message = "Manpower Assignment Fetched Successfully"


class ManpowerAssignmentRetrieveView(CustomGenericRetrieveView):
    serializer_class = ManpowerAssignmentRetrieveSerializer
    queryset = ManpowerAssignment.objects.all()
    success_response_message = "Manpower Assignment Retrieved Successfully"


class ManpowerAssignmentUpdateView(CustomGenericUpdateView):
    serializer_class = ManpowerAssignmentUpdateSerializer
    queryset = ManpowerAssignment.objects.all()
    success_response_message = "Manpower Assignment Updated Successfully"
