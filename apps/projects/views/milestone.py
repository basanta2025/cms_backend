from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import Milestone
from ..serializers import (
    MilestoneCreateSerializer,
    MilestoneListSerializer,
    MilestoneRetrieveSerializer,
    MilestoneUpdateSerializer,
)


class MilestoneCreateView(CustomGenericCreateView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneCreateSerializer
    success_message = "Milestone created successfully."


class MilestoneListView(CustomGenericListView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneListSerializer
    success_message = "Milestones fetched successfully."


class MilestoneRetrieveView(CustomGenericRetrieveView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneRetrieveSerializer
    success_message = "Milestone retrieved successfully."


class MilestoneUpdateView(CustomGenericUpdateView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneUpdateSerializer
    success_message = "Milestone updated successfully."
