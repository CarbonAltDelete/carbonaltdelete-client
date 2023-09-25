from enum import Enum


class ReportFileType(str, Enum):
    PDF = "PDF"
    XLSX = "XLSX"
    DOCX = "DOCX"
    JSON = "JSON"
