from base.serializers import BaseModelSerializer, ExcludeFields
from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import PayType, Worker, WorkerCategory, WorkerDocument
from ..serializers import (
    WorkerCategoryCreateSerializer,
    WorkerCategoryListSerializer,
    WorkerCategoryRetrieveSerializer,
    WorkerCategoryUpdateSerializer,
    WorkerCreateSerializer,
    WorkerDocumentCreateSerializer,
    WorkerDocumentListSerializer,
    WorkerDocumentRetrieveSerializer,
    WorkerDocumentUpdateSerializer,
    WorkerListSerializer,
    WorkerRetrieveSerializer,
    WorkerUpdateSerializer,
)


# Worker Category
class WorkerCategoryCreateView(CustomGenericCreateView):
    serializer_class = WorkerCategoryCreateSerializer
    queryset = WorkerCategory.objects.all()
    success_response_message = "Worker Category Created Successfully"


class WorkerCategoryListView(CustomGenericListView):
    serializer_class = WorkerCategoryListSerializer
    queryset = WorkerCategory.objects.all()
    success_response_message = "Worker Category Fetched Successfully"


class WorkerCategoryRetrieveView(CustomGenericRetrieveView):
    serializer_class = WorkerCategoryRetrieveSerializer
    queryset = WorkerCategory.objects.all()
    success_response_message = "Worker Category Retrieved Successfully"


class WorkerCategoryUpdateView(CustomGenericUpdateView):
    serializer_class = WorkerCategoryUpdateSerializer
    queryset = WorkerCategory.objects.all()
    success_response_message = "Worker Category Updated Successfully"


# Worker
class WorkerCreateView(CustomGenericCreateView):
    serializer_class = WorkerCreateSerializer
    queryset = Worker.objects.all()
    success_response_message = "Worker Created Successfully"


class WorkerListView(CustomGenericListView):
    serializer_class = WorkerListSerializer
    queryset = Worker.objects.all()
    success_response_message = "Worker Fetched Successfully"


class WorkerRetrieveView(CustomGenericRetrieveView):
    serializer_class = WorkerRetrieveSerializer
    queryset = Worker.objects.all()
    success_response_message = "Worker Retrieved Successfully"


class WorkerUpdateView(CustomGenericUpdateView):
    serializer_class = WorkerUpdateSerializer
    queryset = Worker.objects.all()
    success_response_message = "Worker Updated Successfully"


# Worker Document


class WorkerDocumentCreateView(CustomGenericCreateView):
    serializer_class = WorkerDocumentCreateSerializer
    queryset = WorkerDocument.objects.all()
    success_response_message = "WorkerDocument Created Successfully"


class WorkerDocumentListView(CustomGenericListView):
    serializer_class = WorkerDocumentListSerializer
    queryset = WorkerDocument.objects.all()
    success_response_message = "WorkerDocument Fetched Successfully"


class WorkerDocumentRetrieveView(CustomGenericRetrieveView):
    serializer_class = WorkerDocumentRetrieveSerializer
    queryset = WorkerDocument.objects.all()
    success_response_message = "WorkerDocument Retrieved Successfully"


class WorkerDocumentUpdateView(CustomGenericUpdateView):
    serializer_class = WorkerDocumentUpdateSerializer
    queryset = WorkerDocument.objects.all()
    success_response_message = "WorkerDocument Updated Successfully"
