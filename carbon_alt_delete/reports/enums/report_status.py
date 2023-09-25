from enum import Enum


class ReportStatus(str, Enum):
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"
    DONE = "DONE"
