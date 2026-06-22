from base.views.generic_views import (
    CustomGenericCreateView,
    CustomGenericListView,
    CustomGenericRetrieveView,
    CustomGenericUpdateView,
)

from ..models import Document
from ..serializers import (
    DocumentCreateSerializer,
    DocumentListSerializer,
    DocumentRetrieveSerializer,
    DocumentUpdateSerializer,
)


class DocumentCreateView(CustomGenericCreateView):
    queryset = Document.objects.all()
    serializer_class = DocumentCreateSerializer
    success_message = "Document created successfully."


class DocumentListView(CustomGenericListView):
    queryset = Document.objects.all()
    serializer_class = DocumentListSerializer
    success_message = "Documents fetched successfully."


class DocumentRetrieveView(CustomGenericRetrieveView):
    queryset = Document.objects.all()
    serializer_class = DocumentRetrieveSerializer
    success_message = "Document retrieved successfully."


class DocumentUpdateView(CustomGenericUpdateView):
    queryset = Document.objects.all()
    serializer_class = DocumentUpdateSerializer
    success_message = "Document updated successfully."
