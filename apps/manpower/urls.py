from django.urls import include, path

from .views import (
    AttendanceLogCreateView,
    AttendanceLogListView,
    AttendanceLogRetrieveView,
    AttendanceLogUpdateView,
    ManpowerAssignmentCreateView,
    ManpowerAssignmentListView,
    ManpowerAssignmentRetrieveView,
    ManpowerAssignmentUpdateView,
    OverTimeCreateView,
    OverTimeListView,
    OverTimeRetrieveView,
    OverTimeUpdateView,
    WorkerCategoryCreateView,
    WorkerCategoryListView,
    WorkerCategoryRetrieveView,
    WorkerCategoryUpdateView,
    WorkerCreateView,
    WorkerDocumentCreateView,
    WorkerDocumentListView,
    WorkerDocumentRetrieveView,
    WorkerDocumentUpdateView,
    WorkerListView,
    WorkerRetrieveView,
    WorkerUpdateView,
)

attendance_log_patterns = [
    path("create", AttendanceLogCreateView.as_view(), name="attendance-log-create"),
    path("list", AttendanceLogListView.as_view(), name="attendance-log-list"),
    path(
        "retrieve/<int:pk>",
        AttendanceLogRetrieveView.as_view(),
        name="attendance-log-retrieve",
    ),
    path(
        "update/<int:pk>",
        AttendanceLogUpdateView.as_view(),
        name="attendance-log-update",
    ),
]
manpower_assignment_patterns = [
    path(
        "create",
        ManpowerAssignmentCreateView.as_view(),
        name="manpower-assignment-create",
    ),
    path("list", ManpowerAssignmentListView.as_view(), name="manpower-assignment-list"),
    path(
        "retrieve/<int:pk>",
        ManpowerAssignmentRetrieveView.as_view(),
        name="manpower-assignment-retrieve",
    ),
    path(
        "update/<int:pk>",
        ManpowerAssignmentUpdateView.as_view(),
        name="manpower-assignment-update",
    ),
]
overtime_patterns = [
    path("create", OverTimeCreateView.as_view(), name="overtime-create"),
    path("list", OverTimeListView.as_view(), name="overtime-list"),
    path("retrieve/<int:pk>", OverTimeRetrieveView.as_view(), name="overtime-retrieve"),
    path("update/<int:pk>", OverTimeUpdateView.as_view(), name="overtime-update"),
]
worker_category_patterns = [
    path("create", WorkerCategoryCreateView.as_view(), name="worker-category-create"),
    path("list", WorkerCategoryListView.as_view(), name="worker-category-list"),
    path(
        "retrieve/<int:pk>",
        WorkerCategoryRetrieveView.as_view(),
        name="worker-category-retrieve",
    ),
    path(
        "update/<int:pk>",
        WorkerCategoryUpdateView.as_view(),
        name="worker-category-update",
    ),
]
worker_patterns = [
    path("create", WorkerCreateView.as_view(), name="worker-create"),
    path("list", WorkerListView.as_view(), name="worker-list"),
    path("retrieve/<int:pk>", WorkerRetrieveView.as_view(), name="worker-retrieve"),
    path("update/<int:pk>", WorkerUpdateView.as_view(), name="worker-update"),
]
worker_document_patterns = [
    path("create", WorkerDocumentCreateView.as_view(), name="worker-document-create"),
    path("list", WorkerDocumentListView.as_view(), name="worker-document-list"),
    path(
        "retrieve/<int:pk>",
        WorkerDocumentRetrieveView.as_view(),
        name="worker-document-retrieve",
    ),
    path(
        "update/<int:pk>",
        WorkerDocumentUpdateView.as_view(),
        name="worker-document-update",
    ),
]

urlpatterns = [
    path("attendance-log/", include(attendance_log_patterns)),
    path("manpower-assignment/", include(manpower_assignment_patterns)),
    path("overtime/", include(overtime_patterns)),
    path("worker-category/", include(worker_category_patterns)),
    path("worker/", include(worker_patterns)),
    path("worker-document/", include(worker_document_patterns)),
]
