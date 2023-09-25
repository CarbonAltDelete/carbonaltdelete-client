from enum import Enum


class ReportType(str, Enum):
    CARBON_ALT_DELETE = "CARBON_ALT_DELETE"
    ISO14064 = "ISO14064"
    GHG_PROTOCOL = "GHG_PROTOCOL"
    DATA_DUMP = "DATA_DUMP"
    REPORT_DATA = "REPORT_DATA"
