from .attendance import (
    AttendanceLogCreateSerializer,
    AttendanceLogListSerializer,
    AttendanceLogRetrieveSerializer,
    AttendanceLogUpdateSerializer,
)
from .manpower import (
    ManpowerAssignmentCreateSerializer,
    ManpowerAssignmentListSerializer,
    ManpowerAssignmentRetrieveSerializer,
    ManpowerAssignmentUpdateSerializer,
)
from .overtime import (
    OverTimeCreateSerializer,
    OverTimeListSerializer,
    OverTimeRetrieveSerializer,
    OverTimeUpdateSerializer,
)
from .worker import (
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

__all__ = [
    # ATTENDANCE
    "AttendanceLogCreateSerializer",
    "AttendanceLogListSerializer",
    "AttendanceLogRetrieveSerializer",
    "AttendanceLogUpdateSerializer",
    # MANPOWER
    "ManpowerAssignmentCreateSerializer",
    "ManpowerAssignmentListSerializer",
    "ManpowerAssignmentRetrieveSerializer",
    "ManpowerAssignmentUpdateSerializer",
    # OVERTIME
    "OverTimeCreateSerializer",
    "OverTimeListSerializer",
    "OverTimeRetrieveSerializer",
    "OverTimeUpdateSerializer",
    # WORKER CATEGORY
    "WorkerCategoryCreateSerializer",
    "WorkerCategoryListSerializer",
    "WorkerCategoryRetrieveSerializer",
    "WorkerCategoryUpdateSerializer",
    # WORKER
    "WorkerCreateSerializer",
    "WorkerListSerializer",
    "WorkerRetrieveSerializer",
    "WorkerUpdateSerializer",
    # WORKER DOC
    "WorkerDocumentCreateSerializer",
    "WorkerDocumentListSerializer",
    "WorkerDocumentRetrieveSerializer",
    "WorkerDocumentUpdateSerializer",
]
