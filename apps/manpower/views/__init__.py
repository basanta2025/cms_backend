from .attendance import (
    AttendanceLogCreateView,
    AttendanceLogListView,
    AttendanceLogRetrieveView,
    AttendanceLogUpdateView,
)
from .manpower import (
    ManpowerAssignmentCreateView,
    ManpowerAssignmentListView,
    ManpowerAssignmentRetrieveView,
    ManpowerAssignmentUpdateView,
)
from .overtime import (
    OverTimeCreateView,
    OverTimeListView,
    OverTimeRetrieveView,
    OverTimeUpdateView,
)
from .worker import (
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

__all__ = [
    "AttendanceLogCreateView",
    "AttendanceLogListView",
    "AttendanceLogRetrieveView",
    "AttendanceLogUpdateView",
    "ManpowerAssignmentCreateView",
    "ManpowerAssignmentListView",
    "ManpowerAssignmentRetrieveView",
    "ManpowerAssignmentUpdateView",
    "OverTimeCreateView",
    "OverTimeListView",
    "OverTimeRetrieveView",
    "OverTimeUpdateView",
    "WorkerCreateView",
    "WorkerListView",
    "WorkerRetrieveView",
    "WorkerUpdateView",
    "WorkerCategoryCreateView",
    "WorkerCategoryListView",
    "WorkerCategoryRetrieveView",
    "WorkerCategoryUpdateView",
    "WorkerDocumentCreateView",
    "WorkerDocumentListView",
    "WorkerDocumentRetrieveView",
    "WorkerDocumentUpdateView",
]
